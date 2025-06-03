import string
import os

def create_index(filenames):
    index = {}
    file_titles = {}

    for filename in filenames:
        with open(filename, 'r') as file:
            lines = file.readlines()
            title = lines[0].strip()
            file_titles[filename] = title

            for line in lines:
                words = line.strip().split()
                for word in words:
                    word = word.lower().strip(string.punctuation)
                    if word:
                        if word not in index:
                            index[word] = []
                        if filename not in index[word]:
                            index[word].append(filename)

    return index, file_titles

def common(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

def search(index, query):
    words = query.lower().split()

    if not words:
        return []

    result = index.get(words[0], [])
    for word in words[1:]:
        result = common(result, index.get(word, []))

    return result

if __name__ == '__main__':
    folder = 'your_filepath/search_engine/search_results'
    filenames = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.txt')]

    index, file_titles = create_index(filenames)

    query = input("Enter your keyword (empty to quit): ").strip()
    while query:
        results = search(index, query)
        if results:
            print("Search results:")
            for filename in results:
                print(f"- {file_titles[filename]} ({filename})")
        else:
            print("No results found.")

        query = input("\nEnter your keyword (empty to quit): ").strip()