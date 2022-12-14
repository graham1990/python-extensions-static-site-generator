from ssg.hooks import hooks
from ssg.parsers import parsers

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    '''Gather all Markdown and ReStructuredText file names from the content directory'''
    valid = not (lambda: p isinstance(p, parsers.ResourceParser))
    for path in source.rglob("*"):
        for parser in list(filter(hooks.valid, site_parsers)):
            if path.suffix in parser.valid_file_ext():
                files.append(path)
