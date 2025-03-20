import streamlit as st
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


load_dotenv()



endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
key = os.environ["AZURE_LANGUAGE_KEY"]


def analysis_details(doc_result):    
    with st.expander("See detailed results"):  
        positive_mined_opinions = []
        mixed_mined_opinions = []
        negative_mined_opinions = []
    
        for document in doc_result:
            st.write(f"Document Sentiment: {document.sentiment}")
            st.write("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f}".format(
                document.confidence_scores.positive,
                document.confidence_scores.neutral,
                document.confidence_scores.negative
            ))
            st.divider()  # To add a separator between documents

            for sentence in document.sentences:
                st.write(f"Sentence: {sentence.text}")
                st.write(f"Sentence sentiment: {sentence.sentiment}")
                st.write("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}".format(
                    sentence.confidence_scores.positive,
                    sentence.confidence_scores.neutral,
                    sentence.confidence_scores.negative
                ))

                for mined_opinion in sentence.mined_opinions:
                    target = mined_opinion.target
                    st.write(f"'{target.sentiment}'-> target ->'{target.text}'")
                    st.write("Target score:\n......Positive={0:.2f}\n......Negative={1:.2f}".format(
                        target.confidence_scores.positive,
                        target.confidence_scores.negative
                    ))

                    for assessment in mined_opinion.assessments:
                        st.write(f"'{assessment.sentiment}'-> assessment--> '{assessment.text}'")
                        st.write("Assessment score:\n......Positive={0:.2f}\n......Negative={1:.2f}".format(
                            assessment.confidence_scores.positive,
                            assessment.confidence_scores.negative
                        ))

                # st.divider()  # Add a separator between sentences
            st.divider()  # Add a separator between documents
            

# def func(positive,negative,Neutral):
#     def results(value):
#         sum_value = 0
#         for i in range(len(value)):
#             sum_value+=value[i]
#         return sum_value/len(value)
# #     print(len(positive) , len(negative))

#     if len(positive) == len(negative) and len(positive)!=0 and len(negative)!=0:
#         first = results(positive)
#         second = results(negative)
# #         third = results(Neutral.append(0.1))
#         if first > second:
#             return f'Positive : {results(positive)}'
#         else:
#             return f'Negative : {results(negative)}'     
            
#     elif len(positive) > len(negative) and len(positive)>len(Neutral ):
#         return f'Positive : {results(positive)}'
#     elif len(negative)>len(Neutral ):
#         return f'Negative : {results(negative)}'
#     else:
#         return f'Neutral : {results(Neutral )}'