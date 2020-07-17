import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage



def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    filename = f"entries/{title}.md"
    filename_cap = f"entries/{title.capitalize()}.md"
    filename_all_caps = f"entries/{title.upper()}.md"
    
    try:
        #f = default_storage.open(f"entries/{title}.md")
        f = default_storage.open(filename)
        return f.read().decode("utf-8")
        
    except FileNotFoundError:
        try:
            fc = default_storage.open(filename_cap)
            return fc.read().decode("utf-8")
        
        except FileNotFoundError:
            try:
                fac = default_storage.open(filename_all_caps)
                return fac.read().decode("utf-8")
            
            except FileNotFoundError:
                return None

    
def get_title(title):
      s = get_entry(title).split("\n",1)[0]
      return s[2:] 
