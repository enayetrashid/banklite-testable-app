window.addEventListener("DOMContentLoaded", function () {
    clearMessage();
    const currentSession = requireLogin();
    if (!currentSession) {
        return;
    }

    const form = document.getElementById("withdraw-form");
    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        clearMessage();

        const amount = document.getElementById("amount").value;

        try {
            const data = await window.bankliteApi.withdraw(currentSession.account_id, amount);
            showMessage(`Withdrawal completed. New balance: ${formatMoney(data.new_balance)}`, "success");
            form.reset();
        } catch (error) {
            showMessage(error.message, "error");
        }
    });
});
