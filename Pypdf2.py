#!/usr/bin/env python
# coding: utf-8

# In[11]:


import PyPDF2



# In[13]:


PyPDF2.__version__


# In[25]:


# Open the PDF file in binary mode
with open('G_resume.pdf', 'rb') as file:

    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)
    
    # Get the total number of pages in the PDF
    num_pages = len(reader.pages)
    for i in range(num_pages):
        # Get a specific page
        page = reader.pages[i]
        
        # Extract text from the page
        text = page.extract_text()
        
        # Print the extracted text
        print(f"Page {i + 1}:\n{text}\n")
        
    
    

