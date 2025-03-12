# OmniSearch (OS) 🔍
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-blue?logo=github)](https://github.com/sponsors/kevinveenbirkenbach) [![Patreon](https://img.shields.io/badge/Support-Patreon-orange?logo=patreon)](https://www.patreon.com/c/kevinveenbirkenbach) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-Funding-yellow?logo=buymeacoffee)](https://buymeacoffee.com/kevinveenbirkenbach) [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal)](https://s.veen.world/paypaldonate)


OmniSearch (OS) is your ultimate content detective for files of all types! From PDFs and text files to images, spreadsheets, documents, SQLite databases, and more, OS scours your directories to find exactly what you’re looking for – fast and efficiently.

## Features ✨

- **Multi-Format Search:** Search through PDFs, text files, images, Excel files, Word documents, SQLite databases, and more.
- **Flexible Filtering:** Specify file types, ignore certain extensions, or search entire directories.
- **Case & Regex Options:** Toggle between case-sensitive and fixed-string (regex) searches.
- **Verbose Mode:** See the exact commands being executed for complete transparency.
- **Error Handling:** Option to ignore errors and keep searching.
- **JSON Output:** Easily integrate with other tools by outputting results in JSON format.

## Installation 🚀

OmniSearch is available via [Kevin's Package Manager](https://github.com/kevinveenbirkenbach/package-manager). Follow these steps to install it:

1. **Ensure Kevin's Package Manager is installed:**  
   Check out the [package manager repository](https://github.com/kevinveenbirkenbach/package-manager) for setup instructions.

2. **Install OmniSearch using the package manager:**  
   Open your terminal and run:
   ```bash
   pkgmgr install os
   ```
   This installs OmniSearch and makes it globally available under the alias `os`.

## Usage 🛠️

Once installed, you can start searching with the simple alias `os`:

```bash
os /path/to/directory "search term" [options]
```

### Common Options

- `-t, --types`: Specify file types to search in (e.g., `*.txt`, `*.md`, `*.jpg`). If omitted, all files are searched.
- `-p, --paths`: Define the paths to search. If not provided, the current directory is used.
- `-v, --verbose`: Print the executed commands to the console.
- `-i, --ignore`: Ignore errors and continue the search.
- `-s, --skip`: List of file extensions to skip (e.g., `.zip`, `.tar`, `.gz`).
- `-a, --add`: Extend the default list of skipped files with your own.
- `-b, --binary-files`: Treat binary files as text for searching.
- `-c, --case-sensitive`: Perform a case-sensitive search.
- `-f, --fixed`: Use fixed-string search (disables regex).
- `-j, --json`: Output the search results in JSON format.

### Example Commands

- **Basic Search:**  
  Search for the term "example" in the current directory:
  ```bash
  os "example"
  ```

- **Search Specific File Types:**  
  Search for "example" in `.txt` and `.md` files within a specified directory:
  ```bash
  os /path/to/search "example" -t "*.txt" "*.md"
  ```

- **Verbose Search with Error Ignoring:**  
  Get detailed command output and continue despite errors:
  ```bash
  os "example" -v -i
  ```

- **Output in JSON Format:**  
  Get search results as structured JSON:
  ```bash
  os "example" -j
  ```

## License 📄

This project is licensed under the GNU Affero General Public License v3.0. See the [LICENSE](./LICENSE) file for details.

## Author 👤

**Kevin Veen-Birkenbach**  
- Email: [kevin@veen.world](mailto:kevin@veen.world)  
- Website: [https://www.veen.world/](https://www.veen.world/)

## AI Assistance 🤖

This project was developed with the help of AI. Enjoy seamless file content searching with OmniSearch!
