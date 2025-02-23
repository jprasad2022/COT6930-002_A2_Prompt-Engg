![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

# Comparison of 16 prompt engineering methods using Phi-4

* Author: Jay Prasad (Group name: restart)
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)

  
# Research Question 

A comparative analysis of prompts methods in augmenting requirement analysis for surplus lines tax reporting system


## Arguments

#### What is already known about this topic

The existing body of research on prompting has established several effective strategies, including active prompting, prompt chaining, chain-of-thought reasoning, and meta prompting. These methods are known for their ability to guide language models in producing coherent, detailed, and task-specific outputs by providing clear instructions, breaking down complex tasks into manageable steps, and sometimes even encouraging the model to verify its own reasoning before delivering a final response. This foundational knowledge underscores the importance of well-structured prompts that delineate both the desired content and the format of the output, ensuring that the language model remains focused on the task at hand.

#### What this research is exploring

The comparative analysis of the 16 prompts provided new insights into how different prompting approaches can affect the quality of the generated responses. Notably, prompt chaining and automatic prompt engineering emerged as top performers, delivering detailed, state-by-state analyses that were both comprehensive and well-organized. In contrast, prompts that exposed internal reasoning—such as those using chain-of-thought—sometimes compromised the clarity of the final output by including extraneous internal deliberations. Additionally, meta prompts, while useful for instructing subsequent tasks, were less effective as stand-alone responses. This analysis suggests that the balance between explicit instruction and maintaining output brevity is crucial for optimizing response quality.

#### Implications for practice

These findings have significant implications for both research and practical applications. They indicate that refining prompt structures—by emphasizing final, consolidated answers and minimizing exposure of internal reasoning—can lead to more reliable and user-friendly outputs, especially in complex domains like regulatory analysis. Moreover, the insights gained point toward the potential benefits of hybrid approaches that combine the strengths of multiple prompting techniques, as well as the development of standardized evaluation metrics to further assess and improve prompt performance. This research paves the way for future work in optimizing prompt design, model fine-tuning, and the integration of advanced prompting strategies to meet specialized analytical tasks.

# Research Method

There are 16 notebooks using different prompting techniques that execute a language model workflow designed to generate a comprehensive analysis of Surplus Lines Tax regulations across all 50 states. It works in several key steps:
1.	It defines various prompts that instructs the model to verify its understanding by asking clarifying questions if needed before producing a detailed, state-specific requirements analysis. The prompt includes specific instructions covering a general overview, state-by-state details (such as tax rates, filing deadlines, and documentation mandates), compliance obligations, exemptions, and key business challenges.
2.	The code then prints this prompt and calculates its word count. This word count is used as part of the configuration for the model request— to help set the context window size.
3.	Next, it creates a payload by specifying parameters like the target model ("phi4"), a temperature setting of 0.3 for controlled output randomness, the word count as the context size, and a prediction length of up to 5000 tokens.
4.	Finally, the payload is sent to the model which returns both the model’s response and the time taken for the request. The response and the processing time are then printed.
5.	These outputs are stored in **prompt_methods_results** (both html and csv files) for analysis.


# Results

These prompting methods were used to write a comprehensive requirements analysis for Surplus Lines Tax regulations across all 50 states. These responses have been ranked and displayed in order (appearing first means the best and last means the worst). The ranking factors in overall clarity, organization, completeness (including both a general framework and detailed state‐specific information), and whether the output adheres to the final–answer requirement without exposing internal reasoning or off‐topic content. 

1. **Prompt Chaining**: Delivers a detailed, state‑by‑state breakdown that covers tax rates, filing deadlines, documentation requirements, and additional nuances. Its clear organization and final consolidated answer make it the strongest overall.

2. Automatic Prompt Engineering: Offers an extensive, state‑specific analysis with rich details for each state. Despite including an extra calculation prompt at the end, the comprehensive nature of the response earns it a high ranking.

3. Self Consistency: Produces a final, well‐organized consolidated analysis that reflects consistent reasoning across multiple internal paths without exposing those internal details, ensuring clarity and completeness.

4. Program‑aided Language Models: Provides a clear and concise final analysis that covers key regulatory aspects—even if it’s not as granular as the top two, it remains highly useful and structured.

5. Automatic Reasoning: Presents a solid overall overview with key points on taxation, broker licensing, and reporting requirements. While it is less detailed on individual states compared to higher‐ranked responses, it remains a strong summary.

6. Active Prompt: Features a clear overview and organized framework that outlines the essential components. However, it offers less in‑depth state‑specific information than the top responses.

7. Directional Stimulus: Organizes its analysis by regulatory themes and provides concise overviews. Its structure is clear, but the lack of extensive state‑by‑state breakdown limits its completeness.

8. ReAct: Delivers a final answer that appears to capture the overall requirements. Although the details aren’t as extensive as the highest‐ranked outputs, it is moderately well executed.

9. RAG: Uses a retrieval‑augmented approach to synthesize a comprehensive analysis. However, the inclusion of a disclaimer and some extraneous remarks slightly detracts from its polish.

10. Chain of Thought: While it covers many of the necessary elements, this output reveals internal chain‑of‑thought reasoning alongside the final answer, which violates the requirement to show only the consolidated analysis.

11. Few Shots: Attempts to integrate examples from multiple states but ends up with some repetitive and inconsistent entries, reducing overall clarity and cohesion.

12. Reflexion: The output appears less complete and its presentation is somewhat unclear compared to the higher‑ranked responses.

13. Zero Shot: One of response deviates from the subject by discussing unrelated business regulations, making it less useful for the intended analysis.

14. Generate Knowledge: Although it follows a knowledge‐generation approach, the final output drifts off‑topic—covering areas like environmental regulations instead of strictly addressing surplus lines tax.

15. Meta: Provides an excellent meta prompt that could instruct an AI to generate the desired analysis. However, it is not a final consolidated analysis itself, so it ranks lower when considering the task’s requirements.

16. Prompt Template: This output is entirely off‑topic, presenting an analysis of environmental regulations in California rather than the surplus lines tax requirements across all 50 states.

_**PS**: While prompt techniques can enhance responses, as an insurance domain expert, I believe they fall short—likely because the LLM doesn't seem to be thoroughly trained on insurance-specific data. So, one method may be better than others, but even the best ranked method is not adequate._

# Further research

1.	Fine-Tuning on Specialized Regulatory Data: Explore the benefits of fine-tuning language models on domain-specific datasets related to regulatory and tax analysis. This specialization might yield more precise state-specific details and improve the overall completeness of the requirements analysis.

2.	Parameter Sensitivity and Optimization: Conduct experiments to evaluate the impact of key configuration parameters—such as temperature, context window (derived from word count), and prediction length—on the quality of responses. Optimizing these settings may lead to more controlled and reliable outputs.

3.	Hybrid Approaches and Ensemble Methods: Consider combining elements from the best-performing approaches (for example, integrating the detailed state-by-state breakdown from prompt chaining with the succinct structure of program-aided language models) to produce ensemble responses that leverage the strengths of each method.
