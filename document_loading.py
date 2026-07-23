from langchain_docling.loader import DoclingLoader
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

# 1. Enable external plugins in pipeline options
pipeline_options = PdfPipelineOptions()
pipeline_options.allow_external_plugins = True  

# 2. Create the DocumentConverter with the custom options
converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

# 3. Pass the custom converter into DoclingLoader
def load_document(file):
    print(f"Loading document: {file}")
    try:
        print(f"Loading document: {file}")
        loader = DoclingLoader(file, converter=converter)
        data = loader.load()
        return data
    except Exception as e:
        print(f"Error loading document: {e}")
    
    


