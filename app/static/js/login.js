window.addEventListener("DOMContentLoaded", function () {
    clearMessage();

    const currentSession = getCurrentSession();
    if (currentSession) {
        window.location.href = "/dashboard";
        return;
    }

    const form = document.getElementById("login-form");
    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        clearMessage();

        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value;

        try {
            const data = await window.bankliteApi.login(username, password);
            saveCurrentSession(data);
            window.location.href = "/dashboard";
        } catch (error) {
            showMessage(error.message, "error");
        }
    });
});
