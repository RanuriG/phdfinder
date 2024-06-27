from crewai import Task

class ResearchCrewTasks:
    
    def find_universities_task(self, agent, inputs):
      return Task(
          agent=agent,
          description=f"Find all universities which are located at {inputs[0]}, which offers PhDs in the research areas {inputs[2]}, for students who has a GPA of {inputs[1]} or more than that. Only the universities who has a history of offering PhDs.",
          expected_output=f"Provide detailed information on the universities that meet the criteria, "
            "including the names of the universities, their locations, the specific PhD "
            "programs offered, the GPA requirements, and any relevant historical data "
            "on their PhD offerings.",
      )


    def find_professors_task(self, agent, context):
      return Task(
        agent=agent,
        context=context,
        description="Find the suitable supervisors (professors or doctors) from the chosen universities,"
                "who offer PhDs and who do research in {inputs[2]}, while going through their publications and research topics., "
                "Create a description about the details you find."
                "Ensure that the information is accurate and verifiable.",
        expected_output="Provide the following details formatted in markdown for each supervisor found,:\n"
            "- **University**: Name of the university\n"
            "- **Supervisor Name**: Full name of the supervisor\n"
            "- **Research Areas**: Specific areas of research\n"
            "- **Summary of Researches Conducted**: Brief summary of their research work\n"
            "- **Email Address**: Contact email address\n"
            "- **Website URL**: Link to their professional or university profile\n",
        output_file="phd_details.md"


        
  #        1. **University Name: **: University Name
  #   **a. Supervisor: ** Supervisor Name
  #       **Research Areas: ** A list of the supervisor's research areas
  #       **Publications: ** A brief summary of the supervisor's previous publications
  #       **Contact Details: ** Contact Details about the supervisor

  # **b. Supervisor: ** Supervisor Name
  #       **Research Areas: ** A list of the supervisor's research areas
  #       **Publications: ** A brief summary of the supervisor's previous publications
  #       **Contact Details: ** Contact Details about the supervisor
  #       """
      )

    # def writing_task(self, agent, context):
    #     return Task(
    #         agent=agent,
    #         context=context,
    #         description="Synthesize the information provided by the phd_university_finder and enhanced by the phd_professor_finder into a compelling, clear, and well-structured summary. Include key findings and appropriately cite all sources to ensure credibility and traceability.",
    #         expected_output=f"""
    # Comprehensive Summary Report:
    # 1. **Introduction**:
    #   - **Background**: Provide a brief introduction to the topic, outlining the scope and purpose of the initial research.
    #   - **Objectives**: Recap the main objectives of the research to set the context for the findings.

    # 2. **Synthesis of Research and Analysis**:
    #   - **Key Findings**: Present the key findings from the research phase, emphasizing significant data points, trends, and insights.
    #   - **Analytical Enhancements**: Discuss how the analysis phase added value to the initial findings, including any new insights or understandings derived from deeper examination.

    # 3. **Discussion**:
    #   - **Implications**: Explore the implications of the findings in a broader context, discussing potential impacts on the field, industry, or society.
    #   - **Critical Evaluation**: Critically evaluate the findings, noting strengths, weaknesses, and any contentious points that emerged during the research and analysis phases.

    # 4. **Recommendations**:
    #   - **Actionable Steps**: Provide clear, actionable recommendations based on the findings and discussions. These should be practical and tailored to specific stakeholders or policy implications.
    #   - **Future Research**: Suggest areas for future research that could build on the current findings, addressing any gaps or unresolved questions.

    # 5. **Conclusion**:
    #   - **Summary of Findings**: Summarize the main points of the report, reinforcing the significance and reliability of the research conducted.
    #   - **Final Thoughts**: Offer concluding thoughts that underscore the importance of the findings and the potential for future work in this area.

    # 6. **References**:
    #   - **Citations**: Include a detailed list of all sources cited in the document, formatted according to a recognized academic or professional standard.
    #   - **Source Annotations**: Optionally, provide annotations for key sources, explaining their relevance and reliability.

    # 7. **Appendices** (if applicable):
    #   - **Supporting Documents**: Attach any supporting documents, data tables, or supplementary material referenced in the report.
    #   - **Glossary of Terms**: Include a glossary of key terms and definitions used throughout the report for clarity.
    #         """
    #     )




