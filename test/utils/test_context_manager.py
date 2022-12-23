
def test_empty_context_generator():
    from utils.context_manager import ContextManager
    from utils.context_manager import RandomLibraryWithClient
    
    context = ContextManager()
    client = context.get_random_lib_context()
    assert isinstance(client, RandomLibraryWithClient)


def test_existing_context_generator():
    from utils.context_manager import ContextManager
    from utils.context_manager import RandomLibraryWithClient
    
    context= ContextManager()
    client_one = context.get_random_lib_context()
    client_one_addr = id(client_one)
    
    client_two = context.get_random_lib_context()
    client_two_addr = id(client_two)
    assert client_one_addr == client_two_addr