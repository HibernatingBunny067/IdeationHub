from langchain_core.prompts import ChatPromptTemplate

input_prompt = ChatPromptTemplate.from_messages([
    ('system',"you are an expert project mentor, who suggests project ideas that align with the mentee's current skill level and long-term career choice."),
    ("human","""
Generate 1 strucutred project ideas.
     
Skill Level:{skill_level}
Domain:{domain}
Career Goal: {career_goal}
     
Return only structured JSON.
Difficulty must be one of: easy, intermediate or advanced.
     
You MUST return output in this exact JSON format:

{{
  "title": "...",
  "problem_statement": "...",
  "prerequisites": ["..."],
  "features": ["..."],
  "tech_stack": ["..."],
  "difficulty": "easy | intermediate | advanced"
}}

Do not add any other fields.
Do not rename fields.
Do not wrap in markdown.
""")
])

deduplication_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert project idea curator.

Your job:
1. Remove duplicate or highly similar ideas.
2. Rank remaining ideas based on:
   - Alignment with the user's skill level
   - Alignment with long-term career goal
   - Practical build feasibility
3. In any case return 3 or more best ideas.
4. Return count must be greater than 1.

Be strict about uniqueness.
Do not merge ideas.
Remove redundant ones.
"""),

    ("human", """
User Skill Level: {skill_level}
Career Goal: {career_goal}

Here are the generated ideas:

{ideas}

Return output strictly in this JSON format:

{{
  "ideas": [
    {{
      "title": "...",
      "problem_statement": "...",
      "prerequisites": ["..."],
      "features": ["..."],
      "tech_stack": ["..."],
      "difficulty": "easy | intermediate | advanced"
    }}
  ]
}}

Do not add explanations.
Do not include commentary.
Return only valid JSON.
""")
])
