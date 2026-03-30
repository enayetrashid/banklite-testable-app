window.addEventListener("DOMContentLoaded", function () {
    clearMessage();
    const currentSession = requireLogin();
    if (!currentSession) {
        return;
    }

    const form = document.getElementById("deposit-form");
    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        clearMessage();

        const amount = document.getElementById("amount").value;

        try {
            const data = await window.bankliteApi.deposit(currentSession.account_id, amount);
            showMessage(`Deposit completed. New balance: ${formatMoney(data.new_balance)}`, "success");
            form.reset();
        } catch (error) {
            showMessage(error.message, "error");
        }
    });
});
