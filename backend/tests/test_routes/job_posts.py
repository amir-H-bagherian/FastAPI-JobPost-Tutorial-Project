from fastapi import status


def test_job_post_creation(client):
        data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20"
        }
        
        response = client.post('/jobs/create-job/', json=data)
        assert response.status_code == status.HTTP_200_OK 
        assert response.json()["company"] == "doogle"
        assert response.json()["description"] == "python"