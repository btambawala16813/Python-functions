<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Function Reference</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background-color: #fafafa;
            color: #1a1a1a;
            line-height: 1.6;
        }

        .dark-mode {
            background-color: #1a1a1a;
            color: #f0f0f0;
        }

        .dark-mode .search-container {
            background-color: #2d2d2d;
            border-color: #444;
        }

        .dark-mode .search-input {
            background-color: #3a3a3a;
            color: #f0f0f0;
            border-color: #555;
        }

        .dark-mode .search-input::placeholder {
            color: #888;
        }

        .dark-mode .function-card {
            background-color: #2d2d2d;
            border-color: #444;
        }

        .dark-mode .category-btn {
            background-color: #3a3a3a;
            color: #f0f0f0;
            border-color: #555;
        }

        .dark-mode .category-btn.active {
            background-color: #4a4a4a;
            border-color: #666;
        }

        .dark-mode .example-code {
            background-color: #1a1a1a;
            color: #e0e0e0;
            border-color: #444;
        }

        header {
            background-color: #ffffff;
            border-bottom: 1px solid #e0e0e0;
            padding: 30px 20px;
            text-align: center;
        }

        .dark-mode header {
            background-color: #2d2d2d;
            border-bottom-color: #444;
        }

        h1 {
            font-size: 42px;
            font-weight: 300;
            letter-spacing: -1px;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 18px;
            color: #666;
            font-weight: 300;
        }

        .dark-mode .subtitle {
            color: #aaa;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        .controls {
            display: flex;
            gap: 15px;
            margin-bottom: 40px;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
        }

        .search-container {
            flex: 1;
            min-width: 250px;
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .search-icon {
            font-size: 20px;
            color: #999;
        }

        .search-input {
            flex: 1;
            border: none;
            background: transparent;
            font-size: 18px;
            outline: none;
            color: #1a1a1a;
        }

        .search-input::placeholder {
            color: #bbb;
        }

        .mode-toggle {
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            padding: 12px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .mode-toggle:hover {
            background-color: #e8e8e8;
        }

        .dark-mode .mode-toggle {
            background-color: #3a3a3a;
            border-color: #555;
            color: #f0f0f0;
        }

        .dark-mode .mode-toggle:hover {
            background-color: #4a4a4a;
        }

        .categories {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
            flex-wrap: wrap;
            overflow-x: auto;
            padding-bottom: 10px;
        }

        .category-btn {
            background-color: #ffffff;
            border: 1px solid #ddd;
            padding: 12px 20px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 500;
            white-space: nowrap;
            transition: all 0.3s ease;
        }

        .category-btn:hover {
            border-color: #999;
        }

        .category-btn.active {
            background-color: #1a1a1a;
            color: #ffffff;
            border-color: #1a1a1a;
        }

        .dark-mode .category-btn.active {
            background-color: #ffffff;
            color: #1a1a1a;
        }

        .results-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(500px, 1fr));
            gap: 25px;
        }

        .function-card {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 25px;
            transition: all 0.3s ease;
        }

        .function-card:hover {
            border-color: #bbb;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        }

        .dark-mode .function-card:hover {
            box-shadow: 0 4px 12px rgba(255, 255, 255, 0.08);
        }

        .module-badge {
            display: inline-block;
            background-color: #f0f0f0;
            color: #666;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .dark-mode .module-badge {
            background-color: #3a3a3a;
            color: #aaa;
        }

        .function-name {
            font-size: 26px;
            font-weight: 600;
            margin-bottom: 12px;
            color: #1a1a1a;
            font-family: 'Courier New', monospace;
        }

        .dark-mode .function-name {
            color: #e0e0e0;
        }

        .description {
            font-size: 18px;
            color: #555;
            margin-bottom: 20px;
            line-height: 1.6;
        }

        .dark-mode .description {
            color: #bbb;
        }

        .syntax-section {
            margin-bottom: 20px;
        }

        .section-label {
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            color: #999;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }

        .dark-mode .section-label {
            color: #777;
        }

        .syntax {
            font-size: 16px;
            font-family: 'Courier New', monospace;
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 6px;
            border-left: 3px solid #1a1a1a;
            color: #1a1a1a;
            overflow-x: auto;
        }

        .dark-mode .syntax {
            background-color: #1a1a1a;
            border-left-color: #e0e0e0;
            color: #e0e0e0;
        }

        .examples {
            margin-top: 20px;
        }

        .example-item {
            margin-bottom: 15px;
        }

        .example-code {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 6px;
            font-size: 15px;
            font-family: 'Courier New', monospace;
            color: #1a1a1a;
            overflow-x: auto;
            line-height: 1.5;
        }

        .dark-mode .example-code {
            background-color: #1a1a1a;
            border-color: #444;
            color: #e0e0e0;
        }

        .example-output {
            font-size: 15px;
            color: #666;
            margin-top: 8px;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
        }

        .dark-mode .example-output {
            background-color: #2d2d2d;
            color: #aaa;
        }

        .no-results {
            text-align: center;
            padding: 60px 20px;
            color: #999;
            font-size: 20px;
        }

        .dark-mode .no-results {
            color: #777;
        }

        @media (max-width: 768px) {
            .results-container {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 32px;
            }

            .controls {
                flex-direction: column;
            }

            .search-container {
                width: 100%;
            }
        }

        .tags {
            margin-top: 15px;
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .tag {
            background-color: #f0f0f0;
            color: #666;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 13px;
        }

        .dark-mode .tag {
            background-color: #3a3a3a;
            color: #aaa;
        }
    </style>
</head>
<body>
    <header>
        <h1>Python Functions Reference</h1>
        <p class="subtitle">450+ Python functions, methods, and operations at your fingertips</p>
    </header>

    <div class="container">
        <div class="controls">
            <div class="search-container">
                <span class="search-icon">🔍</span>
                <input 
                    type="text" 
                    class="search-input" 
                    id="searchInput" 
                    placeholder="Search functions... (e.g., 'shuffle list', 'read file', 'current time')"
                >
            </div>
            <button class="mode-toggle" id="modeToggle">🌙 Dark Mode</button>
        </div>

        <div class="categories" id="categoriesContainer"></div>

        <div class="results-container" id="resultsContainer"></div>
    </div>

    <script>
        // Complete function database
        const functionsDatabase = [
            // BUILT-IN DATA TYPES
            {
                name: "int()",
                module: "Built-in",
                category: "Data Types",
                description: "Converts value to integer or creates integer object",
                syntax: "int(x, base=10)",
                examples: [
                    { code: 'int("42")', output: "42" },
                    { code: "int(3.9)", output: "3" },
                    { code: 'int("1010", 2)', output: "10 (binary)" }
                ],
                tags: ["conversion", "type", "integer", "number"]
            },
            {
                name: "float()",
                module: "Built-in",
                category: "Data Types",
                description: "Converts value to floating-point number",
                syntax: "float(x)",
                examples: [
                    { code: 'float("3.14")', output: "3.14" },
                    { code: "float(5)", output: "5.0" }
                ],
                tags: ["conversion", "type", "float", "decimal", "number"]
            },
            {
                name: "str()",
                module: "Built-in",
                category: "Data Types",
                description: "Converts value to string",
                syntax: "str(x)",
                examples: [
                    { code: "str(42)", output: '"42"' },
                    { code: "str(3.14)", output: '"3.14"' }
                ],
                tags: ["conversion", "type", "string", "text"]
            },
            {
                name: "bool()",
                module: "Built-in",
                category: "Data Types",
                description: "Converts value to boolean (True/False)",
                syntax: "bool(x)",
                examples: [
                    { code: "bool(1)", output: "True" },
                    { code: "bool(0)", output: "False" },
                    { code: 'bool("")', output: "False" }
                ],
                tags: ["conversion", "type", "boolean", "true", "false"]
            },
            {
                name: "list()",
                module: "Built-in",
                category: "Data Types",
                description: "Creates a list or converts iterable to list",
                syntax: "list(iterable)",
                examples: [
                    { code: 'list("abc")', output: "['a', 'b', 'c']" },
                    { code: "list(range(3))", output: "[0, 1, 2]" }
                ],
                tags: ["list", "array", "collection", "create", "convert"]
            },
            {
                name: "dict()",
                module: "Built-in",
                category: "Data Types",
                description: "Creates dictionary or converts to dict",
                syntax: "dict(mapping)",
                examples: [
                    { code: "dict([('a', 1), ('b', 2)])", output: "{'a': 1, 'b': 2}" },
                    { code: "dict()", output: "{}" }
                ],
                tags: ["dict", "dictionary", "key-value", "object", "create"]
            },
            {
                name: "set()",
                module: "Built-in",
                category: "Data Types",
                description: "Creates set or converts iterable to set",
                syntax: "set(iterable)",
                examples: [
                    { code: "set([1, 1, 2, 3])", output: "{1, 2, 3}" },
                    { code: "set()", output: "set()" }
                ],
                tags: ["set", "unique", "collection", "create", "no duplicates"]
            },
            {
                name: "tuple()",
                module: "Built-in",
                category: "Data Types",
                description: "Creates immutable sequence",
                syntax: "tuple(iterable)",
                examples: [
                    { code: "tuple([1, 2, 3])", output: "(1, 2, 3)" },
                    { code: 'tuple("abc")', output: "('a', 'b', 'c')" }
                ],
                tags: ["tuple", "immutable", "sequence", "create", "fixed"]
            },
            {
                name: "frozenset()",
                module: "Built-in",
                category: "Data Types",
                description: "Creates immutable set",
                syntax: "frozenset(iterable)",
                examples: [
                    { code: "frozenset([1, 2, 3])", output: "frozenset({1, 2, 3})" }
                ],
                tags: ["frozenset", "immutable", "set", "create", "hashable"]
            },
            {
                name: "bytes()",
                module: "Built-in",
                category: "Data Types",
                description: "Creates immutable byte sequence",
                syntax: "bytes(source, encoding)",
                examples: [
                    { code: 'bytes("hello", "utf-8")', output: "b'hello'" },
                    { code: "bytes([72, 101, 108, 108, 111])", output: "b'hello'" }
                ],
                tags: ["bytes", "immutable", "binary", "encode", "create"]
            },

            // STRING METHODS
            {
                name: "str.upper()",
                module: "Built-in",
                category: "String Methods",
                description: "Returns uppercase version of string",
                syntax: "string.upper()",
                examples: [
                    { code: '"hello".upper()', output: '"HELLO"' },
                    { code: '"Python 123".upper()', output: '"PYTHON 123"' }
                ],
                tags: ["string", "case", "uppercase", "convert", "letters"]
            },
            {
                name: "str.lower()",
                module: "Built-in",
                category: "String Methods",
                description: "Returns lowercase version of string",
                syntax: "string.lower()",
                examples: [
                    { code: '"HELLO".lower()', output: '"hello"' },
                    { code: '"PyThOn".lower()', output: '"python"' }
                ],
                tags: ["string", "case", "lowercase", "convert", "letters"]
            },
            {
                name: "str.strip()",
                module: "Built-in",
                category: "String Methods",
                description: "Removes leading and trailing whitespace",
                syntax: "string.strip(chars)",
                examples: [
                    { code: '"  hello  ".strip()', output: '"hello"' },
                    { code: '"xxhelloxx".strip("x")', output: '"hello"' }
                ],
                tags: ["string", "whitespace", "trim", "clean", "remove spaces"]
            },
            {
                name: "str.split()",
                module: "Built-in",
                category: "String Methods",
                description: "Splits string into list by separator",
                syntax: "string.split(sep)",
                examples: [
                    { code: '"a,b,c".split(",")', output: "['a', 'b', 'c']" },
                    { code: '"hello world".split()', output: "['hello', 'world']" }
                ],
                tags: ["string", "split", "separator", "array", "list"]
            },
            {
                name: "str.join()",
                module: "Built-in",
                category: "String Methods",
                description: "Joins iterable elements with string",
                syntax: "separator.join(iterable)",
                examples: [
                    { code: '"-".join(["a", "b", "c"])', output: '"a-b-c"' },
                    { code: '"".join(["hello", "world"])', output: '"helloworld"' }
                ],
                tags: ["string", "join", "combine", "concatenate", "list"]
            },
            {
                name: "str.replace()",
                module: "Built-in",
                category: "String Methods",
                description: "Replaces substring occurrences",
                syntax: "string.replace(old, new, count)",
                examples: [
                    { code: '"hello world".replace("world", "python")', output: '"hello python"' },
                    { code: '"aaa".replace("a", "b", 2)', output: '"bba"' }
                ],
                tags: ["string", "replace", "substitute", "find and replace"]
            },
            {
                name: "str.find()",
                module: "Built-in",
                category: "String Methods",
                description: "Returns index of substring (-1 if not found)",
                syntax: "string.find(substring)",
                examples: [
                    { code: '"hello".find("l")', output: "2" },
                    { code: '"hello".find("x")', output: "-1" }
                ],
                tags: ["string", "search", "index", "find", "locate"]
            },
            {
                name: "str.startswith()",
                module: "Built-in",
                category: "String Methods",
                description: "Checks if string starts with prefix",
                syntax: "string.startswith(prefix)",
                examples: [
                    { code: '"hello".startswith("he")', output: "True" },
                    { code: '"hello".startswith("world")', output: "False" }
                ],
                tags: ["string", "check", "prefix", "begins", "starts"]
            },
            {
                name: "str.endswith()",
                module: "Built-in",
                category: "String Methods",
                description: "Checks if string ends with suffix",
                syntax: "string.endswith(suffix)",
                examples: [
                    { code: '"hello.txt".endswith(".txt")', output: "True" },
                    { code: '"hello.txt".endswith(".pdf")', output: "False" }
                ],
                tags: ["string", "check", "suffix", "ends", "extension"]
            },
            {
                name: "str.isdigit()",
                module: "Built-in",
                category: "String Methods",
                description: "Checks if all characters are digits",
                syntax: "string.isdigit()",
                examples: [
                    { code: '"12345".isdigit()', output: "True" },
                    { code: '"123abc".isdigit()', output: "False" }
                ],
                tags: ["string", "check", "number", "digit", "numeric"]
            },
            {
                name: "str.isalpha()",
                module: "Built-in",
                category: "String Methods",
                description: "Checks if all characters are alphabetic",
                syntax: "string.isalpha()",
                examples: [
                    { code: '"hello".isalpha()', output: "True" },
                    { code: '"hello123".isalpha()', output: "False" }
                ],
                tags: ["string", "check", "letters", "alphabetic", "alpha"]
            },
            {
                name: "str.isalnum()",
                module: "Built-in",
                category: "String Methods",
                description: "Checks if all characters are alphanumeric",
                syntax: "string.isalnum()",
                examples: [
                    { code: '"hello123".isalnum()', output: "True" },
                    { code: '"hello 123".isalnum()', output: "False" }
                ],
                tags: ["string", "check", "letters", "numbers", "alphanumeric"]
            },
            {
                name: "str.count()",
                module: "Built-in",
                category: "String Methods",
                description: "Counts occurrences of substring",
                syntax: "string.count(substring)",
                examples: [
                    { code: '"banana".count("a")', output: "3" },
                    { code: '"hello".count("l")', output: "2" }
                ],
                tags: ["string", "count", "occurrences", "frequency"]
            },
            {
                name: "str.capitalize()",
                module: "Built-in",
                category: "String Methods",
                description: "Capitalizes first character, rest lowercase",
                syntax: "string.capitalize()",
                examples: [
                    { code: '"hello world".capitalize()', output: '"Hello world"' },
                    { code: '"HELLO".capitalize()', output: '"Hello"' }
                ],
                tags: ["string", "case", "capitalize", "first letter"]
            },
            {
                name: "str.title()",
                module: "Built-in",
                category: "String Methods",
                description: "Capitalizes first letter of each word",
                syntax: "string.title()",
                examples: [
                    { code: '"hello world".title()', output: '"Hello World"' },
                    { code: '"python programming".title()', output: '"Python Programming"' }
                ],
                tags: ["string", "case", "title", "capitalize words"]
            },
            {
                name: "str.format()",
                module: "Built-in",
                category: "String Methods",
                description: "Formats string with placeholders",
                syntax: "string.format(*args, **kwargs)",
                examples: [
                    { code: '"Hello {}, age {}".format("John", 25)', output: '"Hello John, age 25"' },
                    { code: '"Hello {name}".format(name="John")', output: '"Hello John"' }
                ],
                tags: ["string", "format", "placeholder", "interpolation"]
            },

            // LIST METHODS
            {
                name: "list.append()",
                module: "Built-in",
                category: "List Methods",
                description: "Adds element to end of list",
                syntax: "list.append(item)",
                examples: [
                    { code: "lst = [1, 2]; lst.append(3)", output: "[1, 2, 3]" }
                ],
                tags: ["list", "add", "append", "insert end"]
            },
            {
                name: "list.extend()",
                module: "Built-in",
                category: "List Methods",
                description: "Adds all elements from iterable to list",
                syntax: "list.extend(iterable)",
                examples: [
                    { code: "lst = [1, 2]; lst.extend([3, 4])", output: "[1, 2, 3, 4]" }
                ],
                tags: ["list", "add", "extend", "combine lists", "merge"]
            },
            {
                name: "list.insert()",
                module: "Built-in",
                category: "List Methods",
                description: "Inserts element at specific index",
                syntax: "list.insert(index, item)",
                examples: [
                    { code: "lst = [1, 2, 3]; lst.insert(1, 99)", output: "[1, 99, 2, 3]" }
                ],
                tags: ["list", "add", "insert", "position"]
            },
            {
                name: "list.remove()",
                module: "Built-in",
                category: "List Methods",
                description: "Removes first occurrence of item",
                syntax: "list.remove(item)",
                examples: [
                    { code: "lst = [1, 2, 3, 2]; lst.remove(2)", output: "[1, 3, 2]" }
                ],
                tags: ["list", "remove", "delete", "element"]
            },
            {
                name: "list.pop()",
                module: "Built-in",
                category: "List Methods",
                description: "Removes and returns element at index",
                syntax: "list.pop(index)",
                examples: [
                    { code: "lst = [1, 2, 3]; lst.pop()", output: "3" },
                    { code: "lst = [1, 2, 3]; lst.pop(0)", output: "1" }
                ],
                tags: ["list", "remove", "get", "last element"]
            },
            {
                name: "list.clear()",
                module: "Built-in",
                category: "List Methods",
                description: "Removes all elements from list",
                syntax: "list.clear()",
                examples: [
                    { code: "lst = [1, 2, 3]; lst.clear()", output: "[]" }
                ],
                tags: ["list", "remove", "clear", "empty"]
            },
            {
                name: "list.index()",
                module: "Built-in",
                category: "List Methods",
                description: "Returns index of first occurrence",
                syntax: "list.index(item)",
                examples: [
                    { code: "lst = [10, 20, 30]; lst.index(20)", output: "1" }
                ],
                tags: ["list", "search", "find", "position", "index"]
            },
            {
                name: "list.count()",
                module: "Built-in",
                category: "List Methods",
                description: "Counts occurrences of item",
                syntax: "list.count(item)",
                examples: [
                    { code: "lst = [1, 2, 2, 3, 2]; lst.count(2)", output: "3" }
                ],
                tags: ["list", "count", "occurrences", "frequency"]
            },
            {
                name: "list.sort()",
                module: "Built-in",
                category: "List Methods",
                description: "Sorts list in-place",
                syntax: "list.sort(reverse=False)",
                examples: [
                    { code: "lst = [3, 1, 2]; lst.sort()", output: "[1, 2, 3]" },
                    { code: "lst = [3, 1, 2]; lst.sort(reverse=True)", output: "[3, 2, 1]" }
                ],
                tags: ["list", "sort", "order", "ascending", "descending"]
            },
            {
                name: "list.reverse()",
                module: "Built-in",
                category: "List Methods",
                description: "Reverses list in-place",
                syntax: "list.reverse()",
                examples: [
                    { code: "lst = [1, 2, 3]; lst.reverse()", output: "[3, 2, 1]" }
                ],
                tags: ["list", "reverse", "backwards", "flip"]
            },
            {
                name: "list.copy()",
                module: "Built-in",
                category: "List Methods",
                description: "Creates shallow copy of list",
                syntax: "list.copy()",
                examples: [
                    { code: "lst1 = [1, 2, 3]; lst2 = lst1.copy()", output: "[1, 2, 3]" }
                ],
                tags: ["list", "copy", "duplicate", "clone"]
            },

            // DICTIONARY METHODS
            {
                name: "dict.keys()",
                module: "Built-in",
                category: "Dictionary Methods",
                description: "Returns view of all keys",
                syntax: "dict.keys()",
                examples: [
                    { code: "d = {'a': 1, 'b': 2}; d.keys()", output: "dict_keys(['a', 'b'])" }
                ],
                tags: ["dict", "keys", "access", "iterate"]
            },
            {
                name: "dict.values()",
                module: "Built-in",
                category: "Dictionary Methods",
                description: "Returns view of all values",
                syntax: "dict.values()",
                examples: [
                    { code: "d = {'a': 1, 'b': 2}; d.values()", output: "dict_values([1, 2])" }
                ],
                tags: ["dict", "values", "access", "iterate"]
            },
            {
                name: "dict.items()",
                module: "Built-in",
                category: "Dictionary Methods",
                description: "Returns view of key-value pairs",
                syntax: "dict.items()",
                examples: [
                    { code: "d = {'a': 1, 'b': 2}; d.items()", output: "dict_items([('a', 1), ('b', 2)])" }
                ],
                tags: ["dict", "items", "key-value", "pairs", "iterate"]
            },
            {
                name: "dict.get()",
                module: "Built-in",
                category: "Dictionary Methods",
                description: "Gets value for key or default",
                syntax: "dict.get(key, default)",
                examples: [
                    { code: "d = {'a': 1}; d.get('a')", output: "1" },
                    { code: "d = {'a': 1}; d.get('b', 'N/A')", output: "'N/A'" }
                ],
                tags: ["dict", "get", "access", "value", "safe"]
            },
            {
                name: "dict.pop()",
                module: "Built-in",
                category: "Dictionary Methods",
                description: "Removes and returns value for key",
                syntax: "dict.pop(key, default)",
                examples: [
                    { code: "d = {'a': 1, 'b': 2}; d.pop('a')", output: "1" }
                ],
                tags: ["dict", "remove", "pop", "delete"]
            },
            {
                name: "dict.update()",
                module: "Built-in",
                category: "Dictionary Methods",
                description: "Updates dict with items from other",
                syntax: "dict.update(other)",
                examples: [
                    { code: "d = {'a': 1}; d.update({'b': 2})", output: "{'a': 1, 'b': 2}" }
                ],
                tags: ["dict", "update", "merge", "combine"]
            },
            {
                name: "dict.clear()",
                module: "Built-in",
                category: "Dictionary Methods",
                description: "Removes all items from dictionary",
                syntax: "dict.clear()",
                examples: [
                    { code: "d = {'a': 1, 'b': 2}; d.clear()", output: "{}" }
                ],
                tags: ["dict", "clear", "empty", "remove all"]
            },
            {
                name: "dict.setdefault()",
                module: "Built-in",
                category: "Dictionary Methods",
                description: "Gets value or sets to default if not found",
                syntax: "dict.setdefault(key, default)",
                examples: [
                    { code: "d = {}; d.setdefault('a', 0)", output: "0" }
                ],
                tags: ["dict", "setdefault", "default", "key"]
            },

            // SET METHODS
            {
                name: "set.add()",
                module: "Built-in",
                category: "Set Methods",
                description: "Adds element to set",
                syntax: "set.add(element)",
                examples: [
                    { code: "s = {1, 2}; s.add(3)", output: "{1, 2, 3}" }
                ],
                tags: ["set", "add", "element"]
            },
            {
                name: "set.remove()",
                module: "Built-in",
                category: "Set Methods",
                description: "Removes element from set (error if not found)",
                syntax: "set.remove(element)",
                examples: [
                    { code: "s = {1, 2, 3}; s.remove(2)", output: "{1, 3}" }
                ],
                tags: ["set", "remove", "delete", "element"]
            },
            {
                name: "set.discard()",
                module: "Built-in",
                category: "Set Methods",
                description: "Removes element (no error if not found)",
                syntax: "set.discard(element)",
                examples: [
                    { code: "s = {1, 2, 3}; s.discard(5)", output: "{1, 2, 3}" }
                ],
                tags: ["set", "remove", "delete", "safe"]
            },
            {
                name: "set.union()",
                module: "Built-in",
                category: "Set Methods",
                description: "Returns union of sets",
                syntax: "set.union(*others)",
                examples: [
                    { code: "s1 = {1, 2}; s2 = {2, 3}; s1.union(s2)", output: "{1, 2, 3}" }
                ],
                tags: ["set", "union", "combine", "merge", "all"]
            },
            {
                name: "set.intersection()",
                module: "Built-in",
                category: "Set Methods",
                description: "Returns common elements",
                syntax: "set.intersection(*others)",
                examples: [
                    { code: "s1 = {1, 2, 3}; s2 = {2, 3, 4}; s1.intersection(s2)", output: "{2, 3}" }
                ],
                tags: ["set", "intersection", "common", "both", "overlap"]
            },
            {
                name: "set.difference()",
                module: "Built-in",
                category: "Set Methods",
                description: "Returns elements in first set only",
                syntax: "set.difference(*others)",
                examples: [
                    { code: "s1 = {1, 2, 3}; s2 = {2, 3, 4}; s1.difference(s2)", output: "{1}" }
                ],
                tags: ["set", "difference", "unique", "not in", "subtract"]
            },

            // NUMBER FUNCTIONS
            {
                name: "abs()",
                module: "Built-in",
                category: "Number Functions",
                description: "Returns absolute value",
                syntax: "abs(x)",
                examples: [
                    { code: "abs(-15)", output: "15" },
                    { code: "abs(-3.5)", output: "3.5" }
                ],
                tags: ["number", "absolute", "value", "positive"]
            },
            {
                name: "round()",
                module: "Built-in",
                category: "Number Functions",
                description: "Rounds number to nearest integer or digits",
                syntax: "round(number, ndigits)",
                examples: [
                    { code: "round(3.7)", output: "4" },
                    { code: "round(3.14159, 2)", output: "3.14" }
                ],
                tags: ["number", "round", "decimal", "precision"]
            },
            {
                name: "pow()",
                module: "Built-in",
                category: "Number Functions",
                description: "Returns base raised to power",
                syntax: "pow(base, exp, mod)",
                examples: [
                    { code: "pow(2, 3)", output: "8" },
                    { code: "pow(5, 2)", output: "25" }
                ],
                tags: ["number", "power", "exponent", "multiply"]
            },
            {
                name: "sum()",
                module: "Built-in",
                category: "Number Functions",
                description: "Returns sum of all elements",
                syntax: "sum(iterable, start)",
                examples: [
                    { code: "sum([1, 2, 3, 4])", output: "10" },
                    { code: "sum([1, 2, 3], start=10)", output: "16" }
                ],
                tags: ["number", "sum", "total", "add all"]
            },
            {
                name: "min()",
                module: "Built-in",
                category: "Number Functions",
                description: "Returns minimum value",
                syntax: "min(iterable) or min(*args)",
                examples: [
                    { code: "min([5, 2, 8, 1])", output: "1" },
                    { code: "min(5, 2, 8)", output: "2" }
                ],
                tags: ["number", "minimum", "lowest", "smallest"]
            },
            {
                name: "max()",
                module: "Built-in",
                category: "Number Functions",
                description: "Returns maximum value",
                syntax: "max(iterable) or max(*args)",
                examples: [
                    { code: "max([5, 2, 8, 1])", output: "8" },
                    { code: "max(5, 2, 8)", output: "8" }
                ],
                tags: ["number", "maximum", "highest", "largest"]
            },
            {
                name: "divmod()",
                module: "Built-in",
                category: "Number Functions",
                description: "Returns quotient and remainder",
                syntax: "divmod(a, b)",
                examples: [
                    { code: "divmod(17, 5)", output: "(3, 2)" }
                ],
                tags: ["number", "divide", "remainder", "quotient"]
            },
            {
                name: "hex()",
                module: "Built-in",
                category: "Number Functions",
                description: "Converts integer to hexadecimal",
                syntax: "hex(x)",
                examples: [
                    { code: "hex(255)", output: "'0xff'" }
                ],
                tags: ["number", "hex", "convert", "base-16"]
            },
            {
                name: "bin()",
                module: "Built-in",
                category: "Number Functions",
                description: "Converts integer to binary",
                syntax: "bin(x)",
                examples: [
                    { code: "bin(10)", output: "'0b1010'" }
                ],
                tags: ["number", "binary", "convert", "base-2"]
            },
            {
                name: "oct()",
                module: "Built-in",
                category: "Number Functions",
                description: "Converts integer to octal",
                syntax: "oct(x)",
                examples: [
                    { code: "oct(8)", output: "'0o10'" }
                ],
                tags: ["number", "octal", "convert", "base-8"]
            },
            {
                name: "ord()",
                module: "Built-in",
                category: "Number Functions",
                description: "Returns Unicode code point of character",
                syntax: "ord(c)",
                examples: [
                    { code: 'ord("A")', output: "65" }
                ],
                tags: ["number", "unicode", "character", "code"]
            },
            {
                name: "chr()",
                module: "Built-in",
                category: "Number Functions",
                description: "Returns character from Unicode code point",
                syntax: "chr(i)",
                examples: [
                    { code: "chr(65)", output: "'A'" }
                ],
                tags: ["number", "unicode", "character", "convert"]
            },

            // SEQUENCE OPERATIONS
            {
                name: "len()",
                module: "Built-in",
                category: "Sequence Operations",
                description: "Returns length of object",
                syntax: "len(object)",
                examples: [
                    { code: "len([1, 2, 3])", output: "3" },
                    { code: 'len("hello")', output: "5" }
                ],
                tags: ["length", "size", "count", "sequence"]
            },
            {
                name: "sorted()",
                module: "Built-in",
                category: "Sequence Operations",
                description: "Returns sorted list from iterable",
                syntax: "sorted(iterable, reverse=False)",
                examples: [
                    { code: "sorted([3, 1, 2])", output: "[1, 2, 3]" },
                    { code: "sorted([3, 1, 2], reverse=True)", output: "[3, 2, 1]" }
                ],
                tags: ["sort", "order", "arrange", "ascending"]
            },
            {
                name: "reversed()",
                module: "Built-in",
                category: "Sequence Operations",
                description: "Returns reversed iterator",
                syntax: "reversed(sequence)",
                examples: [
                    { code: "list(reversed([1, 2, 3]))", output: "[3, 2, 1]" }
                ],
                tags: ["reverse", "backwards", "flip", "iterator"]
            },
            {
                name: "enumerate()",
                module: "Built-in",
                category: "Sequence Operations",
                description: "Returns (index, value) pairs",
                syntax: "enumerate(iterable, start=0)",
                examples: [
                    { code: "list(enumerate(['a', 'b']))", output: "[(0, 'a'), (1, 'b')]" }
                ],
                tags: ["enumerate", "index", "iterate", "pairs"]
            },
            {
                name: "zip()",
                module: "Built-in",
                category: "Sequence Operations",
                description: "Zips multiple sequences together",
                syntax: "zip(*iterables)",
                examples: [
                    { code: "list(zip([1, 2], ['a', 'b']))", output: "[(1, 'a'), (2, 'b')]" }
                ],
                tags: ["zip", "combine", "multiple", "sequences", "tuples"]
            },
            {
                name: "map()",
                module: "Built-in",
                category: "Sequence Operations",
                description: "Applies function to each element",
                syntax: "map(function, iterable)",
                examples: [
                    { code: "list(map(int, ['1', '2']))", output: "[1, 2]" },
                    { code: "list(map(lambda x: x**2, [1, 2, 3]))", output: "[1, 4, 9]" }
                ],
                tags: ["map", "function", "apply", "transform", "each"]
            },
            {
                name: "filter()",
                module: "Built-in",
                category: "Sequence Operations",
                description: "Filters elements where function is True",
                syntax: "filter(function, iterable)",
                examples: [
                    { code: "list(filter(lambda x: x > 2, [1, 2, 3, 4]))", output: "[3, 4]" }
                ],
                tags: ["filter", "select", "condition", "choose"]
            },
            {
                name: "any()",
                module: "Built-in",
                category: "Sequence Operations",
                description: "Returns True if any element is True",
                syntax: "any(iterable)",
                examples: [
                    { code: "any([False, False, True])", output: "True" },
                    { code: "any([False, False, False])", output: "False" }
                ],
                tags: ["any", "condition", "check", "boolean", "or"]
            },
            {
                name: "all()",
                module: "Built-in",
                category: "Sequence Operations",
                description: "Returns True if all elements are True",
                syntax: "all(iterable)",
                examples: [
                    { code: "all([True, True, True])", output: "True" },
                    { code: "all([True, False, True])", output: "False" }
                ],
                tags: ["all", "condition", "check", "boolean", "and"]
            },

            // INPUT/OUTPUT
            {
                name: "input()",
                module: "Built-in",
                category: "Input/Output",
                description: "Gets user input from console",
                syntax: "input(prompt)",
                examples: [
                    { code: 'name = input("Enter name: ")', output: "user types response" }
                ],
                tags: ["input", "user", "console", "read", "prompt"]
            },
            {
                name: "print()",
                module: "Built-in",
                category: "Input/Output",
                description: "Prints output to console",
                syntax: "print(*args, sep=' ', end='\\n')",
                examples: [
                    { code: 'print("Hello", "World")', output: "Hello World" },
                    { code: 'print("a", "b", sep="-")', output: "a-b" }
                ],
                tags: ["print", "output", "console", "display", "show"]
            },
            {
                name: "open()",
                module: "Built-in",
                category: "File Operations",
                description: "Opens file for reading or writing",
                syntax: "open(file, mode, encoding)",
                examples: [
                    { code: "f = open('file.txt', 'r')", output: "<file object>" },
                    { code: "f = open('file.txt', 'w')", output: "<file object>" }
                ],
                tags: ["open", "file", "read", "write", "stream"]
            },

            // MATH MODULE
            {
                name: "math.ceil()",
                module: "math",
                category: "Math Module",
                description: "Rounds up to nearest integer",
                syntax: "math.ceil(x)",
                examples: [
                    { code: "import math; math.ceil(3.2)", output: "4" },
                    { code: "math.ceil(5.0)", output: "5" }
                ],
                tags: ["math", "round", "ceiling", "up"]
            },
            {
                name: "math.floor()",
                module: "math",
                category: "Math Module",
                description: "Rounds down to nearest integer",
                syntax: "math.floor(x)",
                examples: [
                    { code: "import math; math.floor(3.9)", output: "3" },
                    { code: "math.floor(5.0)", output: "5" }
                ],
                tags: ["math", "round", "floor", "down"]
            },
            {
                name: "math.sqrt()",
                module: "math",
                category: "Math Module",
                description: "Returns square root",
                syntax: "math.sqrt(x)",
                examples: [
                    { code: "import math; math.sqrt(16)", output: "4.0" },
                    { code: "math.sqrt(2)", output: "1.414..." }
                ],
                tags: ["math", "square root", "power", "calculate"]
            },
            {
                name: "math.factorial()",
                module: "math",
                category: "Math Module",
                description: "Returns factorial of number",
                syntax: "math.factorial(x)",
                examples: [
                    { code: "import math; math.factorial(5)", output: "120" },
                    { code: "math.factorial(0)", output: "1" }
                ],
                tags: ["math", "factorial", "multiply", "combination"]
            },
            {
                name: "math.gcd()",
                module: "math",
                category: "Math Module",
                description: "Returns greatest common divisor",
                syntax: "math.gcd(*integers)",
                examples: [
                    { code: "import math; math.gcd(48, 18)", output: "6" }
                ],
                tags: ["math", "gcd", "divisor", "common"]
            },
            {
                name: "math.pi",
                module: "math",
                category: "Math Module",
                description: "Pi constant (3.14159...)",
                syntax: "math.pi",
                examples: [
                    { code: "import math; math.pi", output: "3.141592653589793" }
                ],
                tags: ["math", "pi", "constant", "circle"]
            },
            {
                name: "math.e",
                module: "math",
                category: "Math Module",
                description: "Euler's number (2.71828...)",
                syntax: "math.e",
                examples: [
                    { code: "import math; math.e", output: "2.718281828459045" }
                ],
                tags: ["math", "euler", "constant", "e"]
            },
            {
                name: "math.sin()",
                module: "math",
                category: "Math Module",
                description: "Returns sine (x in radians)",
                syntax: "math.sin(x)",
                examples: [
                    { code: "import math; math.sin(math.pi/2)", output: "1.0" }
                ],
                tags: ["math", "sin", "sine", "trigonometry", "radians"]
            },
            {
                name: "math.cos()",
                module: "math",
                category: "Math Module",
                description: "Returns cosine (x in radians)",
                syntax: "math.cos(x)",
                examples: [
                    { code: "import math; math.cos(0)", output: "1.0" }
                ],
                tags: ["math", "cos", "cosine", "trigonometry", "radians"]
            },
            {
                name: "math.tan()",
                module: "math",
                category: "Math Module",
                description: "Returns tangent (x in radians)",
                syntax: "math.tan(x)",
                examples: [
                    { code: "import math; math.tan(math.pi/4)", output: "1.0" }
                ],
                tags: ["math", "tan", "tangent", "trigonometry", "radians"]
            },
            {
                name: "math.log()",
                module: "math",
                category: "Math Module",
                description: "Returns logarithm base-n",
                syntax: "math.log(x, base)",
                examples: [
                    { code: "import math; math.log(8, 2)", output: "3.0" },
                    { code: "math.log(100, 10)", output: "2.0" }
                ],
                tags: ["math", "log", "logarithm", "base"]
            },
            {
                name: "math.exp()",
                module: "math",
                category: "Math Module",
                description: "Returns e raised to power x",
                syntax: "math.exp(x)",
                examples: [
                    { code: "import math; math.exp(1)", output: "2.718..." }
                ],
                tags: ["math", "exponential", "power", "e"]
            },

            // RANDOM MODULE
            {
                name: "random.randint()",
                module: "random",
                category: "Random Module",
                description: "Returns random integer between a and b (inclusive)",
                syntax: "random.randint(a, b)",
                examples: [
                    { code: "import random; random.randint(1, 10)", output: "7 (example)" },
                    { code: "random.randint(1, 100)", output: "42 (example)" }
                ],
                tags: ["random", "integer", "number", "between"]
            },
            {
                name: "random.random()",
                module: "random",
                category: "Random Module",
                description: "Returns random float between 0.0 and 1.0",
                syntax: "random.random()",
                examples: [
                    { code: "import random; random.random()", output: "0.3726... (example)" }
                ],
                tags: ["random", "float", "number", "between", "decimal"]
            },
            {
                name: "random.uniform()",
                module: "random",
                category: "Random Module",
                description: "Returns random float between a and b",
                syntax: "random.uniform(a, b)",
                examples: [
                    { code: "import random; random.uniform(1.0, 5.0)", output: "3.47... (example)" }
                ],
                tags: ["random", "float", "number", "between"]
            },
            {
                name: "random.choice()",
                module: "random",
                category: "Random Module",
                description: "Returns random element from sequence",
                syntax: "random.choice(sequence)",
                examples: [
                    { code: "import random; random.choice([1, 2, 3, 4, 5])", output: "3 (example)" },
                    { code: "random.choice(['apple', 'banana', 'cherry'])", output: "'banana' (example)" }
                ],
                tags: ["random", "choice", "select", "element", "pick"]
            },
            {
                name: "random.shuffle()",
                module: "random",
                category: "Random Module",
                description: "Shuffles list in-place randomly",
                syntax: "random.shuffle(list)",
                examples: [
                    { code: "import random; lst = [1, 2, 3, 4]; random.shuffle(lst)", output: "lst = [3, 1, 4, 2] (example)" }
                ],
                tags: ["random", "shuffle", "randomize", "order", "mix"]
            },
            {
                name: "random.sample()",
                module: "random",
                category: "Random Module",
                description: "Returns k unique random elements",
                syntax: "random.sample(population, k)",
                examples: [
                    { code: "import random; random.sample([1, 2, 3, 4, 5], 3)", output: "[2, 5, 1] (example)" }
                ],
                tags: ["random", "sample", "select", "unique", "elements"]
            },
            {
                name: "random.seed()",
                module: "random",
                category: "Random Module",
                description: "Sets random seed for reproducibility",
                syntax: "random.seed(a)",
                examples: [
                    { code: "import random; random.seed(42); random.randint(1, 100)", output: "same result each time" }
                ],
                tags: ["random", "seed", "reproducible", "consistent"]
            },

            // DATETIME MODULE
            {
                name: "datetime.datetime.now()",
                module: "datetime",
                category: "Datetime Module",
                description: "Returns current date and time",
                syntax: "datetime.datetime.now()",
                examples: [
                    { code: "import datetime; datetime.datetime.now()", output: "2024-03-14 14:30:45.123456" }
                ],
                tags: ["datetime", "current", "time", "now", "today"]
            },
            {
                name: "datetime.date.today()",
                module: "datetime",
                category: "Datetime Module",
                description: "Returns today's date",
                syntax: "datetime.date.today()",
                examples: [
                    { code: "import datetime; datetime.date.today()", output: "2024-03-14" }
                ],
                tags: ["datetime", "date", "today", "current"]
            },
            {
                name: "datetime.datetime.strptime()",
                module: "datetime",
                category: "Datetime Module",
                description: "Parses date string to datetime object",
                syntax: "datetime.datetime.strptime(date_string, format)",
                examples: [
                    { code: 'import datetime; datetime.datetime.strptime("2024-03-14", "%Y-%m-%d")', output: "datetime(2024, 3, 14)" }
                ],
                tags: ["datetime", "parse", "string", "convert", "format"]
            },
            {
                name: "datetime.datetime.strftime()",
                module: "datetime",
                category: "Datetime Module",
                description: "Formats datetime as string",
                syntax: "datetime_object.strftime(format)",
                examples: [
                    { code: 'import datetime; datetime.datetime.now().strftime("%Y-%m-%d")', output: "'2024-03-14'" }
                ],
                tags: ["datetime", "format", "string", "convert"]
            },
            {
                name: "datetime.timedelta()",
                module: "datetime",
                category: "Datetime Module",
                description: "Represents time difference",
                syntax: "datetime.timedelta(days, hours, minutes, ...)",
                examples: [
                    { code: "import datetime; datetime.timedelta(days=1, hours=2)", output: "1 day, 2:00:00" }
                ],
                tags: ["datetime", "timedelta", "difference", "duration"]
            },

            // JSON MODULE
            {
                name: "json.dumps()",
                module: "json",
                category: "JSON Module",
                description: "Converts Python object to JSON string",
                syntax: "json.dumps(obj)",
                examples: [
                    { code: "import json; json.dumps({'a': 1, 'b': 2})", output: "'{\"a\": 1, \"b\": 2}'" }
                ],
                tags: ["json", "convert", "string", "serialize"]
            },
            {
                name: "json.loads()",
                module: "json",
                category: "JSON Module",
                description: "Parses JSON string to Python object",
                syntax: "json.loads(json_string)",
                examples: [
                    { code: "import json; json.loads('{\"a\": 1, \"b\": 2}')", output: "{'a': 1, 'b': 2}" }
                ],
                tags: ["json", "parse", "convert", "deserialize"]
            },
            {
                name: "json.dump()",
                module: "json",
                category: "JSON Module",
                description: "Writes Python object as JSON to file",
                syntax: "json.dump(obj, file)",
                examples: [
                    { code: "import json; json.dump({'a': 1}, open('file.json', 'w'))", output: "writes to file" }
                ],
                tags: ["json", "write", "file", "save"]
            },
            {
                name: "json.load()",
                module: "json",
                category: "JSON Module",
                description: "Reads JSON from file",
                syntax: "json.load(file)",
                examples: [
                    { code: "import json; data = json.load(open('file.json', 'r'))", output: "reads from file" }
                ],
                tags: ["json", "read", "file", "load"]
            },

            // OS MODULE
            {
                name: "os.getcwd()",
