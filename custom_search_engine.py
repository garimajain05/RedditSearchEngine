import os
import sys
import argparse
from exa_py import Exa
from dotenv import load_dotenv

load_dotenv() 

def search_query(query, domains, num_results, search_type):
    api_key = os.getenv("EXA_API_KEY")
    if not api_key:
        print("ERROR: EXA_API_KEY not found. Please set it in your environment or .env file.")
        sys.exit(1)

    try:
        exa = Exa(api_key)
        response = exa.search(
            query=query,
            num_results=num_results,
            type=search_type,
            include_domains=domains,
        )

        if not response.results:
            print("No results found.")
            return

        print("\nTop Search Results:\n")
        for idx, result in enumerate(response.results, 1):
            print(f"{idx}. \033[1m{result.title}\033[0m")
            print(f"   🔗 {result.url}\n")

    except Exception as e:
        print(f"An error occurred while querying Exa: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Exa-Powered Reddit Search Tool")
    parser.add_argument("query", type=str, help="Search query")
    parser.add_argument(
        "--domains", nargs="+", default=["https://www.reddit.com"],
        help="List of domains to include (default: Reddit)"
    )
    parser.add_argument("--results", type=int, default=5, help="Number of results (default: 5)")
    parser.add_argument(
                    "--type", type=str,
                    choices=["keyword", "semantic", "neural", "auto", "magic", "hybrid"],
                    default="keyword",
                    help="Search type: one of keyword, semantic, neural, auto, magic, hybrid")

    args = parser.parse_args()
    #mapping CLI-friendly values to Exa-compatible values
    type_mapping = {
        "semantic": "neural",
        "keyword": "keyword"
    }
    search_type = type_mapping.get(args.type, "keyword")

    search_query(args.query, args.domains, args.results, search_type)


if __name__ == "__main__":
    main()