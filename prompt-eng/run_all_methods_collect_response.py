import os
import glob
import nbformat
import pandas as pd
import re  # Added for regex removal of word count

def extract_notebook_prompt_output_and_time(executed_notebook_path):
    """
    Parses an executed notebook and extracts:
      - Prompt: From the cell that prints the prompt and the word count marker,
                take everything before "Number of words in the prompt:".
      - Output: From a later cell that prints the response and time, take the text
                after "Number of words in the prompt:" (if present) and before "Time taken:".
                Also removes any leading word count number.
      - Time taken: The text after "Time taken:" in that same cell.
    """
    nb = nbformat.read(executed_notebook_path, as_version=4)
    prompt_candidate = None
    response_candidate = None

    # Iterate over cells in order.
    for cell in nb.cells:
        if cell.cell_type == "code" and "outputs" in cell:
            combined_text = ""
            for out in cell["outputs"]:
                if out.output_type == "stream":
                    combined_text += out.get("text", "")
                elif out.output_type == "execute_result":
                    combined_text += out.get("data", {}).get("text/plain", "")
            # Check for the prompt candidate.
            if ("Number of words in the prompt:" in combined_text) and (prompt_candidate is None):
                prompt_candidate = combined_text
            # Check for the response candidate.
            if ("Time taken:" in combined_text) and (response_candidate is None):
                response_candidate = combined_text

    # Extract prompt.
    if prompt_candidate:
        parts = prompt_candidate.split("Number of words in the prompt:")
        prompt_text = parts[0].strip()
    else:
        prompt_text = "No prompt found"

    # Extract output and time.
    if response_candidate:
        # If the response candidate still contains the duplicated prompt info,
        # remove everything before (and including) "Number of words in the prompt:".
        if "Number of words in the prompt:" in response_candidate:
            response_candidate = response_candidate.split("Number of words in the prompt:")[-1].strip()
        parts = response_candidate.split("Time taken:")
        if len(parts) >= 2:
            output_text = parts[0].strip()
            time_text = parts[1].strip()
        else:
            output_text = response_candidate.strip()
            time_text = "No time found"
        # Remove a leading word count number (if present) from the output_text.
        output_text = re.sub(r"^\s*\d+\s*\n", "", output_text)
    else:
        output_text = "No output found"
        time_text = "No time found"

    return prompt_text, output_text, time_text

def main():
    # Process only original notebooks (exclude those starting with "executed_" or "run_all_methods")
    notebooks = [nb for nb in glob.glob("*.ipynb")
                 if not (nb.startswith("executed_") or nb.startswith("run_all_methods"))]
    results = []

    for nb_file in notebooks:
        executed_nb_file = f"executed_{nb_file}"
        print(f"Processing executed notebook: {executed_nb_file} ...")
        prompt_text, output_text, time_text = extract_notebook_prompt_output_and_time(executed_nb_file)
        print(f"Extracted from {executed_nb_file}:")
        print("Prompt:", prompt_text)
        print("Output:", output_text)
        print("Time:", time_text)
        print("=" * 50)
        
        results.append({
            "Notebook": nb_file,
            "Time Taken": time_text,
            "Prompt": prompt_text,
            "Output": output_text
        })

    df = pd.DataFrame(results)
    print("\n=== Prompt Engineering Results Table ===")
    print(df.to_string(index=False))
    df.to_csv("prompt_methods_results.csv", index=False)
    print("\nResults saved to prompt_methods_results.csv")

    # Generate an HTML report using Bootstrap cards (vertical layout)
    cards_html = ""
    for r in results:
        card = f"""
        <div class="card mb-3">
            <div class="card-header"><strong>Notebook:</strong> {r['Notebook']}</div>
            <div class="card-body">
                <p><strong>Time Taken:</strong> {r['Time Taken']}</p>
                <p><strong>Prompt:</strong><br>{r['Prompt'].replace("\n", "<br>")}</p>
                <p><strong>Output:</strong><br>{r['Output'].replace("\n", "<br>")}</p>
            </div>
        </div>
        """
        cards_html += card

    html_report = f"""
    <html>
    <head>
        <title>Prompt Engineering Results</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            body {{
                padding: 20px;
            }}
            .card {{
                margin-bottom: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Prompt Engineering Results</h2>
            {cards_html}
        </div>
    </body>
    </html>
    """

    with open("prompt_methods_results.html", "w", encoding="utf-8") as f:
        f.write(html_report)
    print("Results saved to prompt_methods_results.html")

if __name__ == "__main__":
    main()
