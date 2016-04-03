def swan_io_readSpecFile_s1d(filename):
    '''
    Reads SWAN 1D stationary cartesian coordinates output file
    
    input: file name

    Example:
    from glob import glob
    file_s1d = glob('*.s1d')    
    df       = swan_io_readSpecFile_s1d(file_s1d[0])
    
    author: Saulo Meirelles
    email : oceannimbus@gmail.com
    
    revision: 0
    '''

    import pandas as pd

    specs = dict()
    kw    = dict(columns=('Freq [Hz]',
        'VaDens [m2/Hz]', 
        'CDir [deg]', 
        'Spreading [deg]',
        'KReal [rad/m]',
        'KImag [rad/m]'))

    try:
        f  = open(filename, 'r')
        fd = f.read().split('\n')

        header = fd.pop(0)
        header = fd.pop(0)
        header = fd.pop(0)
        header = fd.pop(0)

        nloc   = int((fd.pop(0).rstrip('\n').split())[0])

        xlocs, ylocs = [], []
        for k in range(nloc):
            l          = fd.pop(0).rstrip('\n').split()
            xloc, yloc = float(l[0]), float(l[1])
            xlocs.append(xloc)
            ylocs.append(yloc)

        linex  = fd.pop(0)

        nfreq  = int((fd.pop(0).rstrip('\n').split())[0])

        freqs = []
        for k in range(nfreq):
            l          = fd.pop(0).rstrip('\n').split()
            freq       = float(l[0])
            freqs.append(freq)

        linex  = fd.pop(0)

        ncols  = int((fd.pop(0).rstrip('\n').split())[0])

        linex  = fd.pop(0)
        linex  = fd.pop(0)

        VaDensExec = float((fd.pop(0).rstrip('\n').split())[0])

        linex  = fd.pop(0)
        linex  = fd.pop(0)

        CDirExec   = float((fd.pop(0).rstrip('\n').split())[0])

        linex  = fd.pop(0)
        linex  = fd.pop(0)

        DsprExec   = float((fd.pop(0).rstrip('\n').split())[0])

        linex  = fd.pop(0)
        linex  = fd.pop(0)

        KrealExec  = float((fd.pop(0).rstrip('\n').split())[0])

        linex  = fd.pop(0)
        linex  = fd.pop(0)

        KimagExec  = float((fd.pop(0).rstrip('\n').split())[0])

        cc       = 0
        while True:    
            lineloc  = fd.pop(0).rstrip('\n').split()
            if 'LOCATION' in lineloc:
                speclocs = []
                for k in range(nfreq):
                    l = fd.pop(0).rstrip('\n').split()
                    l.insert(0, freqs[k])
                    speclocs.append(map(float,l))
                spec_dict = {range(nloc)[cc]: pd.DataFrame(speclocs, **kw)}
                specs.update(spec_dict)
                cc += 1
            else:
                break

    finally:
        f.close()

    df = pd.concat(specs.values(),keys = specs.keys())
    
    return df