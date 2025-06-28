# 🔍 Custom Search Engine using Exa API

A flexible, domain-specific search tool powered by the [Exa API](https://exa.ai), allowing users to run intelligent keyword or semantic searches across selected websites. Currently configured for Reddit, this script is easily extensible to other domains like Medium, Instagram, or Twitter.

## 🚀 Features

* ✅ Keyword and semantic search support
* ✅ Domain-level filtering (e.g., search only Reddit, or add others)
* ✅ CLI with `argparse` for easy usage
* ✅ Outputs formatted, clickable results
* ✅ Uses `.env` file to securely manage API key
* ✅ Error handling and clean output


## 🧠 What is Exa?

[Exa](https://exa.ai) is a developer-first search engine API that provides access to web content through keyword and semantic queries. It's designed for building intelligent tools that require reliable and customizable search functionality.

> You must create an account at [https://exa.ai](https://exa.ai) to obtain your API key.

## 📦 Installation

1. **Clone the repo and navigate to the folder**

   ```bash
   git clone https://github.com/garimajain05/RedditSearchEngine.git
   cd RedditSearchEngine
   ```

2. **Create and activate a virtual environment**

   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   uv pip install -r requirements.txt
   ```

4. **Edit the `.env` file with your Exa API key**

   ```
   EXA_API_KEY=your_exa_api_key_here
   ```

## 🧪 Usage

Run the search script from your terminal:

```bash
python custom_search_engine.py "What is the role of AI in mental health?"
```

### Optional Arguments

| Argument    | Description                                              | Default                      |
| ----------- | -------------------------------------------------------- | ---------------------------- |
| `--domains` | List of websites to restrict search to (space-separated) | `['https://www.reddit.com']` |
| `--results` | Number of results to return                              | `5`                          |
| `--type`    | Type of search: `keyword` or `semantic`                  | `keyword`                    |

### Example with all options:

```bash
python3 custom_search_engine.py "AI and mental health" \
  --domains https://www.reddit.com https://www.medium.com \
  --results 5 \
  --type neural
```

## ✅ Sample Output

```
Top Search Results:

1. Using AI as a free means to assist in Mental Health
   🔗 https://www.reddit.com/r/ArtificialInteligence/comments/12rcn19/using_ai_as_a_free_means_to_assist_in_mental/

2. not only lack effectiveness compared to human therapists
   🔗 https://www.reddit.com/r/psychology/comments/1lb0qlz/exploring_the_dangers_of_ai_in_mental_health_care/

3. People find AI more compassionate and understanding ...
   🔗 https://www.reddit.com/r/Futurology/comments/1jclvtj/people_find_ai_more_compassionate_and/

4. I used to think AI in mental health was a joke..now I see the ...
   🔗 https://www.reddit.com/r/emotionalintelligence/comments/1im27tg/i_used_to_think_ai_in_mental_health_was_a_jokenow/

5. The impacts of AI like CharacterAI will be far larger on ...
   🔗 https://www.reddit.com/r/singularity/comments/1692m2i/the_impacts_of_ai_like_characterai_will_be_far/

```

## 🛠 File Structure

```
RedditSearchEngine
│
├── custom_search_engine.py   #Main searching script
├── .env                      #Store your EXA_API_KEY here (not committed)
├── requirements.txt          #Python dependencies
└── readme.md                 #Project documentation
```