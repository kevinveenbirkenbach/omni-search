# searcher.py
import os
import fnmatch
from handlers.pdf_handler import PDFHandler
from handlers.text_handler import TextHandler
from handlers.xls_handler import XLSHandler
from handlers.doc_handler import DocHandler
from handlers.sqlite_handler import SQLiteHandler
from handlers.odp_handler import ODPHandler
from handlers.metadata_handler import MetadataHandler
from handlers.composite_handler import CompositeHandler
from handlers.pptx_handler import PPTXHandler
from handlers.odt_handler import ODTHandler
from models import FileResult
import pathspec

class Searcher:
    def __init__(
        self,
        search_strings,
        file_types,
        search_paths,
        verbose,
        ignore_errors,
        skip_patterns,
        binary_files,
        case_sensitive,
        fixed,
        respect_gitignore):
        self.search_strings = search_strings
        self.file_types = file_types
        self.setSearchPaths(search_paths)
        self.verbose = verbose
        self.ignore_errors = ignore_errors
        self.skip_patterns = skip_patterns
        self.binary_files = binary_files
        self.case_sensitive = case_sensitive
        self.fixed = fixed
        self.respect_gitignore = respect_gitignore
        self.gitignore_spec = self.load_gitignore() if respect_gitignore else None

    def load_gitignore(self):
        for path in self.search_paths:
            gitignore_path = os.path.join(path, ".gitignore")
            if os.path.exists(gitignore_path):
                with open(gitignore_path) as f:
                    return pathspec.PathSpec.from_lines("gitwildmatch", f)
        return None

    def setSearchPaths(self, search_paths):
        self.search_paths = []
        for search_path in search_paths:
            if not search_path.endswith('/'):
                self.search_paths.append(search_path + '/')
            else:
                self.search_paths.append(search_path)

    def verbose_print(self, *messages):
        if self.verbose:
            print(" ".join(messages))

    def find_all_file_types(self, search_path):
        file_types = set()
        for root, _, files in os.walk(search_path):
            rel_root = os.path.relpath(root, search_path)
            if self.gitignore_spec and self.gitignore_spec.match_file(rel_root):
                continue  # skip ignored directory

            for file in files:
                full_path = os.path.join(rel_root, file)
                if self.gitignore_spec and self.gitignore_spec.match_file(full_path):
                    continue  # skip ignored file
                ext = os.path.splitext(file)[1].lower()
                if ext and not any(fnmatch.fnmatch(ext, pattern.lower()) for pattern in self.skip_patterns):
                    file_types.add(f"*{ext}")
        return list(file_types)

    def search_files(self):
        results = []
        if not self.file_types:
            self.file_types = set()
            for path in self.search_paths:
                self.file_types.update(self.find_all_file_types(path))
            self.file_types = list(self.file_types)

        dispatch = {
            "*.doc": DocHandler,
            "*.pdf": PDFHandler,
            "*.jpeg": CompositeHandler,
            "*.jpg": CompositeHandler,
            "*.png": CompositeHandler,
            "*.xls": XLSHandler,
            "*.odp": ODPHandler,
            "*.odt": ODTHandler,
            "*.pptx": PPTXHandler,
            "*.sqlite": SQLiteHandler,
            "*.mp3": MetadataHandler,
            "*.wav": MetadataHandler,
            "*.flac": MetadataHandler,
            "*.mp4": MetadataHandler,
            "*.avi": MetadataHandler,
            "*.mov": MetadataHandler,
            "*.wmv": MetadataHandler,
        }

        for file_type in self.file_types:
            normalized_file_type = file_type.lower()
            for path in self.search_paths:
                self.verbose_print(f"Searching in {file_type} files in {path} with normalized type {normalized_file_type}...")
                handler_class = dispatch.get(normalized_file_type, TextHandler)
                handler = handler_class(self.search_strings, normalized_file_type, path, self.verbose, self.ignore_errors, self.binary_files, self.case_sensitive, self.fixed)
                results.extend(handler.search())
        return results
