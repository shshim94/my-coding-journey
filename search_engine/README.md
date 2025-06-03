# Search Engine

Welcome to my search engine, which is a simple Python-based search engine built based on Stanford’s "Bajillion" which was provided as a final project idea for [Code in Place](https://codeinplace.stanford.edu) course (CS106A). This program demonstrates how a search engine works under the hood—by indexing text files and allowing users to search for terms found across them.

---

## Project Structure

search_engine_project/
├── searchengine.py # Main Python script with search logic
├── common_elements.py # Helper function to find common list elements
├── celestial_dataset/ # Folder containing searchable .txt files
│ ├── file1.txt
│ ├── file2.txt
│ ...
│ └── file10.txt
└── README.md

---

### How It Works

1. Indexing:  
   The program reads each `.txt` file in the `search_results` folder, extracts words, converts them to lowercase, and removes punctuation. These words are used to build an inverted index.

2. Searching:  
   When the user types a search query (e.g., `stars`, `black holes`), the program returns the list of files that contain **all** the search terms.

---

#### Requirements

- Python 3.x
- OS-independent (works on Windows, macOS, Linux)
- No external packages required

---

##### How to Use

1. Download the Project
    - Clone or download this repository

2. Run the Program
    ```bash
    python3 searchengine.py
    ```

3. Enter a Search Query
    ```
    Enter your keyword (empty to quit): black holes
    Search results:
    - Understanding Black Holes (search_results/file6.txt)
    ```

4. To Exit
    - Just press Enter on an empty prompt

---

###### Example Queries

- `stars`
- `black holes`
- `mars canyon`
- `ice dust`
- `spiral galaxies`

---

####### Credits

Developed as a final project for **Stanford's Code in Place (CS106A)**.  
Inspired by the Bajillion assignment created by Mehran Sahami and Chris Piech.

---