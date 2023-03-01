async function GetLinks() {
    console.log("Get Links");
    const skip = 0;
    const limit = 100;
    const resposne = await fetch(`http://localhost:8080/todo-links/link?skip=${skip}&limit=${limit}`, {
        method: "GET",
        headers: {"Accept": "application/json"}
    });
    const links = await resposne.json();
    return links;
}

async function GetLink() {
    console.log("Get one Link");
    const link_id = document.getElementById('LinkOneId').value;
    const response = await fetch(`http://localhost:8080/todo-links/link/${link_id}`, {
        method: "GET",
        headers: {"Accept": "application/json"}
    });
    const link = await response.json();
    return link;
}

async function CreateLink() {
    console.log("Create Link");
    const link_value = document.getElementById('LinkValue').value;
    const link_creator = document.getElementById('LinkCreator').value;
    const resposne = await fetch(`http://localhost:8080/todo-links/link?user_id=${link_creator}`, {
        method: "POST",
        headers: {"Accept": "application/json", "Content-Type": "application/json"},
        body: JSON.stringify({
            value: link_value,
            user_id: link_creator
        })
    });
    const link = await resposne.json();
    return link;
}

async function DeleteLink() {
    console.log("Delete Link");
    const link_id = document.getElementById('LinkId').value;
    const link_user_id = document.getElementById('LinkUserId').value;
    const response = await fetch(`http://localhost:8080/todo-links/link/${link_id}?user_id=${link_user_id}`, {
        method: "DELETE",
        headers: {"Accept": "application/json"}
    });
    const link = await response.json();
    return link;
}




async function GetUsers() {
    console.log("Get Users");
    const skip = 0;
    const limit = 100;
    const resposne = await fetch(`http://localhost:8080/todo-users/user?skip=${skip}&limit=${limit}`, {
        method: "GET",
        headers: { "Accept": "application/json"}
    });
    const users = await resposne.json();
    return users;
}

async function GetUser() {
    console.log("Get User");
    const id = document.getElementById('UserId').value;
    console.log(id);
    const resposne = await fetch(`http://localhost:8080/todo-users/user/${id}`, {
        method: "GET",
        headers: { "Accept": "application/json"}    
    });
    const user = await resposne.json();
    return user;
}

async function CreateUser() {
    console.log("Create User");
    const user_name = document.getElementById('UserName').value;
    const resposne = await fetch(`http://localhost:8080/todo-users/user`, {
        method: "POST",
        headers: {"Accept": "application/json", "Content-Type": "application/json"},
        body: JSON.stringify({
            name: user_name
        })
    });
    const user = await resposne.json();
    return user;
}