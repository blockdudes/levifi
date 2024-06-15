from cosmpy.aerial.wallet   import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey
from cosmpy.aerial.contract import LedgerContract
from cosmpy.aerial.client   import LedgerClient, NetworkConfig, Address
from cosmpy.crypto.keypairs import PrivateKey

def get_wallet_and_contract():
    prefix = 'osmo'

    private_key = PrivateKey(bytes.fromhex("d1b90f4c8834c582cc103f3412278a03e9057e10f5af3dd0e523f51b7a55967c"))
    wallet = LocalWallet(private_key, prefix=prefix)
    
    cfg = NetworkConfig(
        chain_id="osmo-test-5",
        url="grpc+https://grpc.osmotest5.osmosis.zone",
        fee_minimum_gas_price=1,
        fee_denomination="uosmo",
        staking_denomination="uosmo",
    )
    
    ledger_client = LedgerClient(cfg)
    address = Address('osmo19gg7wyv4fyevu8z7948yqhkcqjeffru0ufg4e3e5ryscxd5u2vfqmj7hxw')
    contract = LedgerContract(None, ledger_client, address)
    
    return wallet, contract