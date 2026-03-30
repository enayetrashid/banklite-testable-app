window.addEventListener("DOMContentLoaded", function () {
    clearMessage();
    const currentSession = requireLogin();
    if (!currentSession) {
        return;
    }

    const form = document.getElementById("transfer-form");
    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        clearMessage();

        const targetAccountId = document.getElementById("target_account_id").value.trim();
        const amount = document.getElementById("amount").value;

        try {
            const data = await window.bankliteApi.transfer(
                currentSession.account_id,
                targetAccountId,
                amount,
            );
            showMessage(`Transfer completed. New balance: ${formatMoney(data.new_balance)}`, "success");
            form.reset();
        } catch (error) {
            showMessage(error.message, "error");
        }
    });
});
