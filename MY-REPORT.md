![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

# Comparison of 16 prompt engineering methods using LLM (phi4)
1-liner description of your project

<!-- WHEN APPLICABLE, REMOVE THE COMMENT MARK AND COMPLETE
This is a response to the Assignment part of the COURSE.
-->

* Author: Jay Prasad (Group name: restart)
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)

  
# Research Question 

A comparative analysis of prompts methods in augmenting requirement analysis for surplus lines tax reporting system


## Arguments

#### What is already known about this topic

* you could do {something} to achieve {some result}
* the challenges of {doing something}
* the possibility of {doing something else}
* ...

#### What this research is exploring

<!-- Free-format; use the topics that are applicable to your exploration  -->

* we employ {some technique}
* we are building {something}
* we are exploring {some idea or technology}

#### Implications for practice

<!-- Free-format; use the topics that are applicable to your exploration  -->

* it will be easier to {do something}
* it will optimize {some process}
* we will better understand {some process}
* ...

# Research Method

Describe how you are building this research process.

<!-- WHEN APPLICABLE AND AVAILABLE -->

# Results

These prompting methods were used to write a comprehensive requirements analysis for Surplus Lines Tax regulations across all 50 states. These responses have been ranked and displayed in order (appearing first means the best and last means the worst). The ranking factors in overall clarity, organization, completeness (including both a general framework and detailed state‐specific information), and whether the output adheres to the final–answer requirement without exposing internal reasoning or off‐topic content. 

1. Prompt Chaining: Delivers an exceptionally detailed, state‑by‑state breakdown that covers tax rates, filing deadlines, documentation requirements, and additional nuances. Its clear organization and final consolidated answer make it the strongest overall.

2. Automatic Prompt Engineering: Offers an extensive, state‑specific analysis with rich details for each state. Despite including an extra calculation prompt at the end, the comprehensive nature of the response earns it a high ranking.

3. Self Consistency: Produces a final, well‐organized consolidated analysis that reflects consistent reasoning across multiple internal paths without exposing those internal details, ensuring clarity and completeness.

4. Program‑aided Language Models: Provides a clear and concise final analysis that covers key regulatory aspects—even if it’s not as granular as the top two, it remains highly useful and structured.

automatic_reasoning.ipynb
 • Presents a solid overall overview with key points on taxation, broker licensing, and reporting requirements. While it is less detailed on individual states compared to higher‐ranked responses, it remains a strong summary.

active_prompt.ipynb
 • Features a clear overview and organized framework that outlines the essential components. However, it offers less in‑depth state‑specific information than the top responses.

directional_stimulus.ipynb
 • Organizes its analysis by regulatory themes and provides concise overviews. Its structure is clear, but the lack of extensive state‑by‑state breakdown limits its completeness.

react.ipynb
 • Delivers a final answer that appears to capture the overall requirements. Although the details aren’t as extensive as the highest‐ranked outputs, it is moderately well executed.

rag.ipynb
 • Uses a retrieval‑augmented approach to synthesize a comprehensive analysis. However, the inclusion of a disclaimer and some extraneous remarks slightly detracts from its polish.

chain_of_thought.ipynb
 • While it covers many of the necessary elements, this output reveals internal chain‑of‑thought reasoning alongside the final answer, which violates the requirement to show only the consolidated analysis.

few_shots.ipynb
 • Attempts to integrate examples from multiple states but ends up with some repetitive and inconsistent entries, reducing overall clarity and cohesion.

reflexion.ipynb
 • The output appears less complete and its presentation is somewhat unclear compared to the higher‑ranked responses.

zero_shot.ipynb
 • One version of the zero‑shot response deviates from the subject by discussing unrelated business regulations, making it less useful for the intended analysis.

generate_knowledge.ipynb
 • Although it follows a knowledge‐generation approach, the final output drifts off‑topic—covering areas like environmental regulations instead of strictly addressing surplus lines tax.

meta.ipynb
 • Provides an excellent meta prompt that could instruct an AI to generate the desired analysis. However, it is not a final consolidated analysis itself, so it ranks lower when considering the task’s requirements.

prompt_template.ipynb
 • This output is entirely off‑topic, presenting an analysis of environmental regulations in California rather than the surplus lines tax requirements across all 50 states.

# Further research

Describe what we could do next and propose new ideas for further research.
