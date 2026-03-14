
def test_create_task_success(client, task_payload):

    response = client.post("/tasks", json=task_payload)

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == task_payload["title"]
    assert data["description"] == task_payload["description"]
    assert data["user_id"] == task_payload["user_id"]
    
def test_get_tasks(client, task):

    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == task.title
    
def test_get_task_by_id(client, task):

    response = client.get(f"/tasks/{task.id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task.id
    assert data["title"] == task.title
    
def test_get_task_not_found(client):

    response = client.get("/tasks/999")

    assert response.status_code == 404
    
def test_delete_task(client, task):

    response = client.delete(f"/tasks/{task.id}")

    assert response.status_code == 200

    response = client.get("/tasks")

    data = response.json()

    assert len(data) == 0
    
def test_delete_task_already_deleted(client, task):

    client.delete(f"/tasks/{task.id}")

    response = client.delete(f"/tasks/{task.id}")

    assert response.status_code == 400