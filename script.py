import cmdstanpy

model = cmdstanpy.CmdStanModel(stan_file="bernoulli.stan")
mcmc = model.sample(data="bernoulli.data.json")
