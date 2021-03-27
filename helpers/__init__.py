IBMQ_PROVIDER = None


def get_ibmq_provider():
    global IBMQ_PROVIDER
    if IBMQ_PROVIDER is None:
        from qiskit import IBMQ
        IBMQ_PROVIDER = IBMQ.load_account()
    return IBMQ_PROVIDER
