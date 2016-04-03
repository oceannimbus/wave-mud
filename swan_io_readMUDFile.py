def swan_io_readMUDFile(filename):
    '''
    Reads SWAN 1D stationary cartesian coordinates mud file
    
    input: file name

    Example:
    from glob import glob
    
    file_mud = glob('MUDFile*')    
    df       = swan_io_readMUDFile(file_mud[0])
    
    author: Saulo Meirelles
    email : oceannimbus@gmail.com
    
    revision: 0
    '''

    specs = dict()
    kw    = dict(columns=('Freq [Hz]',
        'KReal [rad/m]',
        'KImag [rad/m]'))

    try:
        f  = open(filename, 'r')
        fd = f.read().split('\n')

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

        KRealExec = float((fd.pop(0).rstrip('\n').split())[0])

        linex  = fd.pop(0)
        linex  = fd.pop(0)

        KImagExec   = float((fd.pop(0).rstrip('\n').split())[0])

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
    df.reindex
    
    return df