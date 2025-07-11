import requests
import json

# === CONFIG ===
OPENCTI_URL = "https://demo.opencti.io"
API_TOKEN = ""  # replace with your token

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

# GraphQL Query: https://demo.opencti.io/public/graphql for testing queries
QUERY = """
query GetArtifacts {
  stixCyberObservables(types: ["Artifact"], first: 100) { # replace with different limit, eg first: 20
    edges {
      node {
        id
        entity_type
        created_at
        observable_value
        ... on Artifact {
          mime_type
          hashes {
            algorithm
            hash
          }
        }
      }
    }
  }
}
"""

def fetch_file_hashes():
    response = requests.post(
        f"{OPENCTI_URL}/graphql",
        headers=HEADERS,
        json={"query": QUERY}
    )

    try:
        data = response.json()
        #print("\nRaw Response:") # Testing raw response
        #print(json.dumps(data, indent=2)) # Testing raw response
    except Exception as e:
        print("Failed to parse JSON:", e)
        print("Raw response text:", response.text)
        return

    if "data" not in data:
        print("'data' field missing. Likely a GraphQL or auth issue.")
        return

    files = data["data"]["stixCyberObservables"]["edges"]

    for file in files:
        node = file["node"]
        print("\n--- FILE ---")
        print("ID:", node["id"])
        #print("Type:", node["entity_type"])
        print("Created at:", node["created_at"])
        print("Type:", node["mime_type"])
        print("Hashes:")
        for h in node.get("hashes", []):
            print(f"  {h['algorithm']}: {h['hash']}")

if __name__ == "__main__":
    fetch_file_hashes()
