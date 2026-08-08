const API = "http://127.0.0.1:8000";

function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch(API + "/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);

        // save token
        localStorage.setItem("token", data.access_token);

        alert("Login successful!");

        // go to home page
        window.location.href = "index.html";
    });
}

function loadVouchers() {
    fetch(API + "/vouchers")
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById("list");
        list.innerHTML = "";

        data.forEach(v => {
            const item = document.createElement("li");

            item.innerHTML = `
                ${v.title} - ₹${v.selling_price}
                <button onclick="buy(${v.id})">Buy</button>
            `;

            list.appendChild(item);
        });
    });
}

function buy(id) {
    const token = localStorage.getItem("token");

    fetch(API + "/buy/" + id, {
        method: "POST",
        headers: {
            "Authorization": "Bearer " + token
        }
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
    });
}

function loadMyVouchers() {
    const token = localStorage.getItem("token");

    fetch(API + "/my-vouchers", {
        headers: {
            "Authorization": "Bearer " + token
        }
    })
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById("myList");
        list.innerHTML = "";

        data.forEach(v => {
            const item = document.createElement("li");

            item.innerHTML = `
                ${v.title} - ₹${v.selling_price}
            `;

            list.appendChild(item);
        });
    });
}

function logout() {
    localStorage.removeItem("token");
    window.location.href = "login.html";
}

function loadVouchers() {
    fetch(API + "/vouchers")
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById("list");
        list.innerHTML = "";

        data.forEach(v => {
            const item = document.createElement("div");
            item.className = "card";

            item.innerHTML = `
                <h3>${v.title}</h3>
                <p>₹${v.selling_price}</p>
                <button onclick="buy(${v.id})">Buy</button>
            `;

            list.appendChild(item);
        });
    });
}

function loadMyVouchers() {
    const token = localStorage.getItem("token");

    fetch(API + "/my-vouchers", {
        headers: {
            "Authorization": "Bearer " + token
        }
    })
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById("myList");
        list.innerHTML = "";

        data.forEach(v => {
            const item = document.createElement("div");
            item.className = "card";

            item.innerHTML = `
                <h3>${v.title}</h3>
                <p>₹${v.selling_price}</p>
            `;

            list.appendChild(item);
        });
    });
}

function signup() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch(API + "/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || "Signup successful");

        // go to login page
        window.location.href = "login.html";
    });
}