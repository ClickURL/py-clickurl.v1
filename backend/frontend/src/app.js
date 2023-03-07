// ------------------------------------------------
// For Link entity (begin) 
// ------------------------------------------------

// Function to call from html page to create a new record in the database
function Create() {
    console.log("Create Link");
    const link_value = document.getElementById('LinkValue').value;
    const link_user_id = document.getElementById('LinkUserId').value;
    CreateLink(link_value, link_user_id);
}

// Function directly to create a new record in the database
async function CreateLink(link_value, link_user_id) {

    const response = await fetch(`http://localhost:8080/todo-links/link?user_id=${link_user_id}`, {
        method: "POST",
        headers: {"Accept": "application/json", "Content-Type": "application/json"},
        body: JSON.stringify({
            value: link_value,
            user_id: link_user_id
        })
    });
    if (response.ok) {
        const link = await response.json();
        document.getElementById("link_table_body").append(add_item_link(link));
        return link;
    }
    else {
        const error = await response.json();
        console.log(error.message);
    }
}

// Function directly to get all record from the database
async function GetLinks() {
    const skip = 0;
    const limit = 100;
    const response = await fetch(`http://localhost:8080/todo-links/link?skip=${skip}&limit=${limit}`, {
        method: "GET",
        headers: {"Accept": "application/json"}
    });
    if (response.ok) {
        const links = await response.json();
        const rows = document.getElementById("link_table_body");
        links.forEach(link => rows.append(add_item_link(link)));
        return links;
    }
    else {
        const error = await response.json();
        console.log(error.message);
    }
}
// Function directly to remove record from the database
async function DeleteLink(link_id, link_user_id) {
    const response = await fetch(`http://localhost:8080/todo-links/link/${link_id}?user_id=${link_user_id}`, {
        method: "DELETE",
        headers: {"Accept": "application/json"}
    });
    if (response.ok) {
        const link = await response.json();
        document.querySelector(`tr[data-rowid = '${link.id}']`).remove();
        return link;
    }
    else {
        const error = await response.json();
        alert(error.detail);
        console.log(response.error);
    }
}

// Function that displays records from the database on the html page
function add_item_link(link) {
    const table_row = document.createElement("tr");
    table_row.setAttribute("data-rowid", link.id);

    const id_td = document.createElement("td");
    id_td.append(link.id);
    table_row.append(id_td);

    const link_td = document.createElement("td");
    const link_a = document.createElement("a");
    link_a.setAttribute("href", link.value);
    link_a.append(link.value);
    link_td.append(link_a);
    table_row.append(link_td);

    const user_id_td = document.createElement("td")
    user_id_td.append(link.created_by);
    table_row.append(user_id_td);

    const user_name_td = document.createElement("td")
    user_name_td.append(link.creator.name);
    table_row.append(user_name_td);

    const delete_td = document.createElement("td");

    const delete_link = document.createElement("button");
    delete_link.append("Delete");
    delete_link.addEventListener("click", async () => {
        const link_user_id = document.getElementById('LinkUserId').value;
        await DeleteLink(link.id, link_user_id);
    });
    delete_td.append(delete_link);

    table_row.appendChild(delete_td);

    return table_row;
}

// Call function to displays all records from the database on the html page when html page load/reload
GetLinks();


// additional options are not presented on this page "todo-links.html"

function GetAll() {
    console.log("Get Links");
    GetLinks();
}

function GetOne() {
    console.log("Get one Link");
    const link_id = document.getElementById('LinkOneId').value;
    GetLink(link_id);
}

function Remove() {
    console.log("Delete Link");
    const link_id = document.getElementById('LinkId').value;
    const link_user_id = document.getElementById('LinkUserId').value;
    DeleteLink(link_id, link_user_id);
}

async function GetLink(link_id) {
    const response = await fetch(`http://localhost:8080/todo-links/link/${link_id}`, {
        method: "GET",
        headers: {"Accept": "application/json"}
    });
    if (response.ok) {
        const link = await response.json();
        return link;
    }
    else {
        const error = await response.json();
        console.log(error.message);
    }
}

// ------------------------------------------------
// For Link entity (end) 
// ------------------------------------------------


// ------------------------------------------------
// For User entity (begin) 
// ------------------------------------------------

async function GetUsers() {
    console.log("Get Users");
    const skip = 0;
    const limit = 100;
    const response = await fetch(`http://localhost:8080/todo-users/user?skip=${skip}&limit=${limit}`, {
        method: "GET",
        headers: { "Accept": "application/json"}
    });
    const users = await response.json();
    return users;
}

async function GetUser() {
    console.log("Get User");
    const id = document.getElementById('UserId').value;
    console.log(id);
    const response = await fetch(`http://localhost:8080/todo-users/user/${id}`, {
        method: "GET",
        headers: { "Accept": "application/json"}    
    });
    const user = await response.json();
    return user;
}

async function CreateUser() {
    console.log("Create User");
    const user_name = document.getElementById('UserName').value;
    const response = await fetch(`http://localhost:8080/todo-users/user`, {
        method: "POST",
        headers: {"Accept": "application/json", "Content-Type": "application/json"},
        body: JSON.stringify({
            name: user_name
        })
    });
    const user = await response.json();
    return user;
}

// ------------------------------------------------
// For User entity (end)
// ------------------------------------------------