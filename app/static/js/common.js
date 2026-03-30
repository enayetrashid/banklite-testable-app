function getCurrentSession() {
    const rawValue = sessionStorage.getItem("bankliteSession");
    if (!rawValue) {
        return null;
    }

    try {
        return JSON.parse(rawValue);
    } catch (error) {
        sessionStorage.removeItem("bankliteSession");
        return null;
    }
}

function saveCurrentSession(data) {
    sessionStorage.setItem("bankliteSession", JSON.stringify(data));
}

function clearCurrentSession() {
    sessionStorage.removeItem("bankliteSession");
}

function requireLogin() {
    const currentSession = getCurrentSession();
    const path = window.location.pathname;

    if (!currentSession && path !== "/login") {
        window.location.href = "/login";
        return null;
    }

    return currentSession;
}

function showMessage(message, category) {
    const box = document.getElementById("message-box");
    if (!box) {
        return;
    }

    box.innerHTML = `<p class="message ${category}">${message}</p>`;
}

function clearMessage() {
    const box = document.getElementById("message-box");
    if (!box) {
        return;
    }

    box.innerHTML = "";
}

function formatMoney(value) {
    return Number(value).toFixed(2);
}

window.addEventListener("DOMContentLoaded", function () {
    const logoutLink = document.getElementById("logout-link");
    if (logoutLink) {
        logoutLink.addEventListener("click", function (event) {
            event.preventDefault();
            clearCurrentSession();
            window.location.href = "/login";
        });
    }
});
