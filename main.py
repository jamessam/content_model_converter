import datetime
import os
import re
import sys

import contentful_management
import pandas as pd

def clean_name(name):
  '''This function strips special characters out of content type names. Essential for the tab creation process.'''
  clean_name = re.sub('\W+',' ', name )
  return clean_name

def main(SPACE_ID, CF_ENV, PAT):
  cma = contentful_management.Client(PAT)
  content_types = cma.content_types(SPACE_ID, CF_ENV).all()
  if len(content_types.items) < 1: 
    sys.exit('There\'s no content types in this space.')

  file_name = f'{SPACE_ID}_content_model_{datetime.date.today()}.xlsx'
  writer = pd.ExcelWriter(file_name)

  for content_type in content_types:
      ct = content_type.to_json()
      name = clean_name(ct['name'])
      fields = ct['fields']
      df = pd.DataFrame(fields)
      df.to_excel(writer, name, index=False)
  writer.save()


if __name__ == '__main__':
  if len(sys.argv) != 3:
      raise SyntaxError("Please supply a space ID and environment ID.")
  
  SPACE_ID = sys.argv[1]
  CF_ENV = sys.argv[2]
  PAT = os.environ['PERSONAL_ACCESS_TOKEN']

  if len(SPACE_ID) != 12:
    raise SyntaxError("Invalid space ID.")

  if not (PAT.startswith('CFPAT-', 0, 6)):
    raise SyntaxError("Invalid PAT.")
  
  main(SPACE_ID, CF_ENV, PAT)