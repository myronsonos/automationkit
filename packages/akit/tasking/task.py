

"""
    [exec:spawn].[quit|cont].[expect|ignore].[local|player[expr]|players|].action
"""

import copy
import threading


class ChainLink:

    NAME = None
    CHAIN_NAME = None

    def __init__(self, chain = None):
        self._chain = chain
        if self._chain is None:
            self._chain = self._get_chain(self.CHAIN_NAME)
        return

    def __call__(self, *args, **kwargs):
        self._chain.append((self, args, kwargs))
        return self

    def _execute(self):

        this_type = type(self)
        type_name = this_type.__name__

        # Setup
        print("{}: Setting Up".format(type_name))

        # Do work and get result
        yield 0

        # Teardown
        print("{}}: Tearing Down".format(type_name))

    def _activate(self):

        result = 0
        try:
            nxt_inst, nxt_args, nxt_kwargs = self._pop()
            result = next(nxt_inst._execute(nxt_args, nxt_kwargs))
        except:
            result = -1
        finally:
            pass

        return result

    def _get_chain(self, chain_name):

        if chain_name is None:
            raise Exception("Only root chain links have a chain name.")

        chain = None

        this_thread = threading.current_thread()
        if hasattr(this_thread, chain_name):
            chain = this_thread.chain
        else:
            chain = []
            setattr(this_thread, chain_name, chain)

        return chain


    def _pop(self):
        items = None, None, None
        if len(self._chain) > 0:
            self._chain.pop(0)
        return items

class LocalLink(ChainLink):
    """
    """

    NAME = "local"

    def __init__(self, chain=None):
        super(LocalLink, self).__init__(chain=chain)
        return

    def __call__(self, *args, **kwargs):
        self._chain.append((self, args, kwargs))
        return self

    def run_command(self, command, timeout=None):
        self._command = command
        self._timeout = timeout

        self._activate()

        return

    def _execute(self):

        result = 0

        print(self._command)

        return result

class ExpectLink(ChainLink):
    """
    """

    NAME = "expect"

    def __init__(self, chain=None):
        super(ExpectLink, self).__init__(chain=chain)
        self._result = None
        return

    def __call__(self, *args, result=0, **kwargs):
        self._result=result

        pack_kwargs = copy.copy(kwargs)
        pack_kwargs["result"] = result

        self._chain.append((self, args, pack_kwargs))
        return self

    def local(self, *args, **kwargs):
        link = LocalLink(chain=self._chain)
        link(*args, **kwargs)
        return link

    def _execute(self):

        result = 0
        try:
            result = next(self._pop())
        except:
            result = -1
        finally:
            pass

        return result


class ContinueLink(ChainLink):
    """
    """

    NAME = "cont"

    def expect(self, *args, **kwargs):
        link = ExpectLink(chain=self._chain)
        link(*args, **kwargs)
        return link

    def __call__(self, *args, **kwargs):
        self._chain.append((self, args, kwargs))
        return self

    def _execute(self):

        result = 0
        try:
            result = next(self._pop())
        except:
            result = -1
        finally:
            pass

        return result

class ExecLink(ChainLink):
    """
    """

    NAME = "exec"
    CHAIN_NAME = "chain_exec"

    def cont(self, *args, **kwargs):
        link = ContinueLink(chain=self._chain)
        link(*args, **kwargs)
        return link

    def __call__(self, *args, **kwargs):
        self._chain.append((self, args, kwargs))
        return self

    def _execute(self):

        this_type = type(self)
        type_name = this_type.__name__

        # Setup
        print("{}: Setting Up".format(type_name))

        results = 0
        try:
            results = next(self._pop())
        except:
            results = -1
        finally:
            pass

        # Do work and get result
        yield results

        # Teardown
        print("{}: Tearing Down".format(type_name))

    def _execute(self):

        results = None
        try:
            result = next(self._pop())
        except:
            result = -1
        finally:
            pass

        return result


exec = ExecLink()

if __name__ == "__main__":

    exec().cont().expect(result=0).local().run_command("echo blah")
