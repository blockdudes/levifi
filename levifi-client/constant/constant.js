import * as paillierBigint from "paillier-bigint";

export const pubkey = new paillierBigint.PublicKey(
    1678481375462202042297541766968126908461n,
    1678481375462202042297541766968126908462n
);

export const leverage_contract_address = "archway1gxu4xla8w8zmjlp6lu6ztzlfetzhz6gfz7hz0tupqhxmwa4t0g8q000ref";
export const usdc_contract_address = "archway1hcctxstwswmctpk0zkj0f06fy3he38akujp5pvxf3754wl7pyw9sjmzyh5";

export const usdc_token_name = "USDC"
export const native_token_name = "ARCH";

export const tokens = [
    { name: "usdc", address: usdc_token_name },
    { name: "native", address: native_token_name }
]
export const queryBalanceMethods = [
    { method: 'user_collateral_token_balance', key: 'collateral_balance' },
    { method: 'user_wrapped_token_balance', key: 'wrapped_leverage_balance' },
    { method: 'user_borrow_token_balance', key: 'borrow_balance' },
    { method: 'user_v_token_balance', key: 'v_token_balance' }
]

