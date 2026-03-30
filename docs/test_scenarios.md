# Test Scenarios

## Login
- Verify valid login works through the login API
- Verify invalid password returns an error message
- Verify empty username is rejected

## Dashboard
- Verify dashboard reads balance using the balance API

## Deposit
- Verify valid deposit updates the balance
- Verify text amount is rejected

## Withdraw
- Verify insufficient funds are blocked

## Transfer
- Verify valid transfer updates sender balance
- Verify own-account transfer is blocked

## Transactions
- Verify transaction history returns created records
