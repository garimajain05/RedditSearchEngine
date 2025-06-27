# 🔍 Reddit Search using Exa API

This is a simple Python script to perform keyword-based web search using the [Exa API](https://exa.ai/), currently scoped to Reddit. The script fetches top search results and displays the title and URL for each.

---

## 📦 Installation

1. **Create a virtual environment (recommended)**

   ```bash
   uv venv
   source .venv/bin/activate
   ```

2. **Install dependencies**

   ```bash
   uv pip install -r requirements.txt
   ```

3. **Run the script**

   ```bash
   python main.py
   ```

---

## 🧠 What is Exa?

[Exa](https://exa.ai) is a developer-first search API that allows you to build semantic and keyword-based search directly into your applications. It gives you fine-grained control over the domains, number of results, types of search (keyword vs semantic), and more.

To use this script, you’ll need to:

* Create an account on [https://exa.ai](https://exa.ai)
* Retrieve your API key from your dashboard
* Replace `'YOUR KEY'` in the script with your actual key

---

## ⚙️ Modifications You Can Make

You can easily modify the script to tailor the search results to your needs:

* **Add more domains**:
  You can include more domains like Instagram, Medium, etc.

  ```python
  include_domains=[
    'https://www.reddit.com',
    'https://www.instagram.com',
    'https://medium.com',
  ]
  ```

* **Change number of results**:
  Increase or decrease the number of results.

  ```python
  num_results=10  # change from 5 to 10
  ```

* **Use semantic search instead of keyword search**:

  ```python
  type='semantic'  # instead of 'keyword'
  ```

* **Filter by specific time ranges (if supported)** or other metadata by exploring more parameters from the Exa documentation.

---

## ✅ Example Output

```
$ python3 main.py
Enter your Search query: What is the role of AI in mental health services?

Title: The Role of AI in Mental Health Treatment: A Game ...
URL: https://www.reddit.com/r/socialpsychology/comments/1g9r618/title_the_role_of_ai_in_mental_health_treatment_a/

Title: Psychologist's Take: AI's Impact on Mental Healthcare
URL: https://www.reddit.com/r/aiwars/comments/1glup4a/psychologists_take_ais_impact_on_mental/

Title: People Are Turning to AI Therapy—Here's Why It Might Be ...
URL: https://www.reddit.com/r/ArtificialInteligence/comments/1i8cuf0/more_people_are_turning_to_ai_therapyheres_why_it/

Title: Using AI as a free means to assist in Mental Health
URL: https://www.reddit.com/r/ArtificialInteligence/comments/12rcn19/using_ai_as_a_free_means_to_assist_in_mental/

Title: People find AI more compassionate and understanding ...
URL: https://www.reddit.com/r/Futurology/comments/1jclvtj/people_find_ai_more_compassionate_and/
```