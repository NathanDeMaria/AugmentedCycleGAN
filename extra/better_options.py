class Options:
    dataroot = '/data2/datasets/'
    batchSize = 2
    continue_train = True
    which_epoch = 0
    epoch_count = 0
    niter = 25
    niter_decay = 25
    beta1 = .5
    lr = .0002

    no_lsgan = False
    lambda_A = 1.
    lambda_B = 1.
    lambda_z_B = .025

    use_sigmoid = True

    ngf = 32
    nef = 32
    ndf = 64
    nlatent = 16

    input_nc = 3
    output_nc = 3

    which_model_netD = 'basic'
    which_model_netG = 'resnet'
    norm = 'instance'
    use_dropout = True
    max_gnorm = 5000
    stoch_enc = True
    gpu_ids = []

    z_gan = 1
    enc_A_B = 1

    expr_dir = 'nope, not doing this'
