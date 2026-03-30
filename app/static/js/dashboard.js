window.addEventListener("DOMContentLoaded", async function () {
    clearMessage();
    const currentSession = requireLogin();
    if (!currentSession) {
        return;
    }

    try {
        const data = await window.bankliteApi.getBalance(currentSession.account_id);
        document.getElementById("username-value").textContent = data.username;
        document.getElementById("full-name-value").textContent = data.full_name;
        document.getElementById("account-id-value").textContent = data.account_id;
        document.getElementById("balance-value").textContent = formatMoney(data.balance);
    } catch (error) {
        showMessage(error.message, "error");
    }
});
