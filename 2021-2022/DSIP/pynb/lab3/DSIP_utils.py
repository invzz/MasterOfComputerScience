# uncomment the line above when you're ready

class LTI:
    """ Linear time-invariant system object """    
    def __init__(self, name, imp_resp):
        self.name = name
        self.h = imp_resp
        self.H = self._setFrequencyResponse()
        
    def transform(self, x):
        return signal.fftconvolve(x, self.h, mode='same') #/ np.sum(np.abs(x))
    
    def high_pass(self, x):
        return 

    def _setFrequencyResponse(self):
        return np.fft.fft(self.h)/np.sum(np.abs(self.h))
