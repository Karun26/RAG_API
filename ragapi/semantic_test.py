import requests

def test_kubernetes_query():
    response = requests.post("http://127.0.0.1:8000/query?q=What is Kubernetes?")
    
    if response.status_code != 200:
        raise Exception(f"Server returned {response.status_code}: {response.text}")
    
    answer = response.json()["answer"]

    # Check for key concepts
    assert "orchestration" in answer.lower(), "Missing 'orchestration' keyword"
    assert "container" in answer.lower(), "Missing 'container' keyword"

    print("✅ Kubernetes query test passed")

    response2 = requests.post("http://127.0.0.1:8000/query?q=Who is Karun?")
    
    if response2.status_code != 200:
        raise Exception(f"Server returned {response2.status_code}: {response2.text}")
    
    answer2 = response2.json()["answer"]

    # Check for key concepts
    assert "AI/ML" in answer2.lower(), "Missing 'AI/ML' keyword"
    assert "Engineer" in answer2.lower(), "Missing 'Engineer' keyword"

    print("✅ Karun query test passed")

if __name__ == "__main__":
    test_kubernetes_query()
    print("All semantic tests passed!")
