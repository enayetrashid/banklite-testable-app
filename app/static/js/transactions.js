window.addEventListener("DOMContentLoaded", async function () {
    clearMessage();
    const currentSession = requireLogin();
    if (!currentSession) {
        return;
    }

    try {
        const data = await window.bankliteApi.getTransactions(currentSession.account_id);
        const transactions = data.transactions;
        const table = document.getElementById("transactions-table");
        const body = document.getElementById("transactions-body");
        const emptyState = document.getElementById("empty-state");

        body.innerHTML = "";

        if (!transactions.length) {
            table.classList.add("hidden");
            emptyState.classList.remove("hidden");
            return;
        }

        emptyState.classList.add("hidden");
        table.classList.remove("hidden");

        transactions.forEach(function (item) {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${item.type}</td>
                <td>${formatMoney(item.amount)}</td>
                <td>${item.message}</td>
            `;
            body.appendChild(row);
        });
    } catch (error) {
        showMessage(error.message, "error");
    }
});
