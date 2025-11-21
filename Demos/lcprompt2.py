from langchain_core.prompts import PromptTemplate

# Create a prompt template that has multiple input variables
multi_var_prompt = PromptTemplate(
     input_variables=["customerName", "feedbackFromCustomer"],
     template="""
     Human: Create an email to {customerName} in response to the following customer service feedback that was received from the customer: 
     <customer_feedback> 
          {feedbackFromCustomer}
     </customer_feedback>
     Assistant:"""
)
# Pass in values to the input variables
prompt = multi_var_prompt.format(customerName="John Doe",
          feedbackFromCustomer="""Hello AnyCompany, 
     I am very pleased with the recent experience I had when I called your customer support.
      I got an immediate call back, and the representative was very knowledgeable in fixing the problem. 
     We are very happy with the response provided and will consider recommending it to other businesses.
     """
)

print(prompt)