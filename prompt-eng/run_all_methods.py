import os
import glob
import papermill as pm
import nbformat
import pandas as pd
from _pipeline import create_payload, model_req  # if needed in the notebooks

def execute_notebook(notebook_path, output_path):
    """
    Execute a notebook using papermill and save the executed copy.
    No parameters are injected in this version.
    """
    pm.execute_notebook(
        input_path=notebook_path,
        output_path=output_path,
    )

def main():
    notebooks = glob.glob("*.ipynb")
    results = []

    for nb_file in notebooks:
        # Skip our own driver script if stored as a notebook
        if nb_file.startswith("run_all_methods"):
            continue

        executed_nb_file = f"executed_{nb_file}"
        print(f"Running notebook: {nb_file} ...")
        execute_notebook(nb_file, executed_nb_file)
        print(f"Executed notebook saved as: {executed_nb_file}")

        results.append({
            "Notebook": nb_file,
            "Status": "Executed"
        })

    df = pd.DataFrame(results)
    print("\n=== Notebook Execution Results ===")
    print(df.to_string(index=False))

    # Save results to CSV (optional)
    df.to_csv("notebook_execution_results.csv", index=False)
    print("\nResults saved to notebook_execution_results.csv")

    # Generate an HTML table from the DataFrame with Bootstrap styling
    html_table = df.to_html(index=False, classes="table table-striped", border=0)

    # Save the HTML report to a file
    with open("notebook_execution_results.html", "w") as f:
        f.write(f"""
<html>
<head>
    <title>Notebook Execution Results</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {{ padding-top: 20px; }}
        h2 {{ margin-bottom: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <h2>Notebook Execution Results</h2>
        {html_table}
    </div>
</body>
</html>
""")
    print("Results saved to notebook_execution_results.html")

if __name__ == "__main__":
    main()
