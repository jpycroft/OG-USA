VAR_LABELS = {'Y': 'GDP ($Y_t$)', 'C': 'Consumption ($C_t$)',
              'L': 'Labor ($L_t$)',
              'G': 'Government Expenditures ($G_t$)',
              'TR': 'Lump sum transfers ($TR_t$)',
              'B': 'Wealth ($B_t$)', 'I_total': 'Investment ($I_t$)',
              'K': 'Capital Stock ($K_t$)',
              'K_d': 'Domestically-owned Capital Stock ($K^d_t$)',
              'K_f': 'Foreign-owned Capital Stock ($K^f_t$)',
              'D': 'Government Debt ($D_t$)',
              'D_d': 'Domestically-owned Gov Debt ($D^d_t$)',
              'D_f': 'Foreign-owned Gov Debt ($D^f_t$)',
              'r': 'Real interest rate ($r_t$)',
              'r_gov': 'Real interest rate on gov debt ($r_{gov,t}$)',
              'r_hh': 'Real interest rate on HH portfolio ($r_{hh,t}$)',
              'w': 'Wage rate', 'BQ': 'Aggregate bequests ($BQ_{j,t}$)',
              'total_revenue': 'Total tax revenue ($REV_t$)',
              'business_revenue': 'Business tax revenue',
              'IITpayroll_revenue': 'IIT and payroll tax revenue',
              'n_mat': 'Labor Supply ($n_{j,s,t}$)',
              'c_path': 'Consumption ($c_{j,s,t}$)',
              'bmat_splus1': 'Savings ($b_{j,s+1,t+1}$)',
              'bq_path': 'Bequests ($bq_{j,s,t}$)',
              'bmat_s': 'Savings ($b_{j,s,t}$)',
              'y_before_tax_mat': 'Before tax income',
              'etr_path': 'Effective Tax Rate ($ETR_{j,s,t}$)',
              'mtrx_path':
              'Marginal Tax Rate, Labor Income ($MTRx_{j,s,t}$)',
              'mtry_path':
              'Marginal Tax Rate, Capital Income ($MTRy_{j,s,t}$)',
              'tax_path':
              'Total Taxes',
              'nssmat': 'Labor Supply ($\\bar{n}_{j,s}$)',
              'bssmat_s': 'Savings ($\\bar{b}_{j,s}$)',
              'bssmat_splus1': 'Savings ($\\bar{b}_{j,s+1}$)',
              'cssmat': 'Consumption ($\\bar{c}_{j,s}$)',
              'yss_before_tax_mat': 'Before-tax Income',
              'etr_ss': 'Effective Tax Rate ($\\bar{ETR}_{j,s}$)',
              'mtrx_ss':
              'Marginal Tax Rate, Labor Income ($\\bar{MTRx}_{j,s}$)',
              'mtry_ss':
              'Marginal Tax Rate, Capital Income ($\\bar{MTRy}_{j,s}$)',
              'ETR': 'Effective Tax Rates',
              'MTRx': 'Marginal Tax Rates on Labor Income',
              'MTRy': 'Marginal Tax Rates on Capital Income',
              'Yss': 'GDP ($\\bar{Y}$)',
              'Css': 'Consumption ($\\bar{C}$)',
              'Lss': 'Labor ($\\bar{L}$)',
              'Gss': 'Government Expenditures ($\\bar{G}$)',
              'TR_ss': 'Lump sum transfers, ($\\bar{TR}$)',
              'Bss': 'Wealth ($\\bar{B}$)',
              'Iss_total': 'Investment ($\\bar{I}$)',
              'Kss': 'Capital Stock ($\\bar{K}$)',
              'K_d_ss':
                  'Domestically-owned Capital Stock ($\\bar{K}^d$)',
              'K_f_ss': 'Foreign-owned Capital Stock ($\\bar{K}^f$)',
              'Dss': 'Government Debt ($\\bar{D}$)',
              'D_d_ss': 'Domestically-owned Gov Debt ($\\bar{D}^d$)',
              'D_f_ss': 'Foreign-owned Gov Debt ($\\bar{D}^f$)',
              'rss': 'Real interest rate ($\\bar{r}$)',
              'r_gov_ss':
                  'Real interest rate on gov debt ($\\bar{r}_{gov}$)',
              'r_hh_ss':
                  'Real interest rate on HH portfolio ($\\bar{r}_{hh}$)',
              'wss': 'Wage rate ($\\bar{w}$)',
              'BQss': 'Aggregate bequests ($\\bar{BQ}_{j}$)',
              'total_revenue_ss': 'Total tax revenue ($\\bar{REV}$)',
              'business_revenue': 'Business tax revenue',
              'IITpayroll_revenue': 'IIT and payroll tax revenue',
              'debt_service_ss':
                  'Debt service cost ($\\bar{r}_{gov}\\bar{D}$)',
              'D/Y': 'Debt to GDP ratio', 'T_Pss': 'Government Pensions'
              }

ToGDP_LABELS = {'D': 'Debt-to-GDP ($D_{t}/Y_t$)',
                'D_d': 'Domestically-owned Debt-to-GDP ($D^d_{t}/Y_t$)',
                'D_f': 'Foreign-owned Debt-to-GDP ($D^f_{t}/Y_t$)',
                'G': 'Govt Spending-to-GDP ($G_{t}/Y_t$)',
                'K': 'Capital-Output Ratio ($K_{t}/Y_t$)',
                'K_d':
                'Domestically-owned Capital-Output Ratio ($K^d_{t}/Y_t$)',
                'K_f':
                'Foreign-owned Capital-Output Ratio ($K^f_{t}/Y_t$)',
                'C': 'Consumption-Output Ratio ($C_{t}/Y_t$)',
                'I': 'Investment-Output Ratio ($I_{t}/Y_t$)',
                'total_revenue': 'Tax Revenue-to-GDP ($REV_{t}/Y_t$)'}

GROUP_LABELS = {0: '0-25%', 1: '25-50%', 2: '50-70%', 3: '70-80%',
                4: '80-90%', 5: '90-99%', 6: 'Top 1%'}

CBO_UNITS = {
    'Y': r'Billions of \$', 'r': 'Percent', 'w_growth': 'Percent',
    'L_growth': 'Percent', 'I_total': r'Billions of \$', 'L': '2012=100',
    'C': r'Billions of \$', 'T_P': r'Billions of \$',
    'G': r'Billions of \$', 'iit_revenue': r'Billions of \$',
    'payroll_tax_revenue': r'Billions of \$',
    'business_revenue': r'Billions of \$', 'wL': r'Billions of \$',
    'D': r'Billions of \$'}

PARAM_LABELS = {
    # 'Gamma': ['Initial distribution of savings', r'\hat{\Gamma}_{0}'],
    # 'N': ['Initial population', 'N_{0}'],
    'omega': ['Initial population by age',
              r'\left{\omega_{s,0}\right}_{s=1}^{S}'],
    # 'fert_rates': ['Fertility rates by age',
    #                r'\left{f_{s}\right}_{s=1}^{S}'],
    'imm_rates': ['Immigration rates by age',
                  r'\left{i_{s}\right}_{s=1}^{S}'],
    'rho': ['Mortality rates by age',
            r'\left{\rho_{s}\right}_{s=1}^{S}'],
    'e': ['Deterministic ability process',
          r'\left{\e_{j,s}\right}_{j,s=1}^{J,S}'],
    'lambdas': ['Lifetime income group percentages',
                r'\left{\lambda_{j}\right}_{j=1}^{J}'],
    'J': ['Number of lifetime income groups', 'J'],
    'S': ['Maximum periods in economically active individual life',
          'S'],
    'E': ['Number of periods of youth economically outside the model',
          'E'],
    'retire': ['Retirement age (period)', 'R'],
    'ltilde': ['Maximum hours of labor supply', r'\tilde{l}'],
    'beta': ['Discount factor', r'\beta'],
    'sigma': ['Coefficient of constant relative risk aversion',
              r'\sigma'],
    'frisch': ['Frisch elasticity of labor supply', r'\nu'],
    'b_ellipse': ['Scale parameter in utility of leisure', 'b'],
    'upsilon': ['Shape parameter in utility of leisure', r'\upsilon'],
    # 'k': ['Constant parameter in utility of leisure', 'k'],
    'chi_n': ['Disutility of labor level parameters',
              r'\left{\chi^{n}_{s}\right}_{s=1}^{S}'],
    'chi_b': ['Utility of bequests level parameters',
              r'\left{\chi^{b}_{j}\right}_{j=1}^{J}'],
    'Z': ['Total factor productivity', 'Z'],
    'gamma': ['Capital share of income', r'\gamma'],
    'epsilon': ['Elasticity of substitution between capital and labor',
                r'\varepsilon'],
    'delta': ['Capital depreciation rate', r'\delta'],
    'g_y': ['Growth rate of labor augmenting technological progress',
            r'g_{y}'],
    'tau_payroll': ['Payroll tax rate', r'\tau^{p}_{t}'],
    # 'theta': ['Replacement rate by average income',
    #           r'\left{\theta_{j}\right}_{j=1}^{J}'],
    'tau_bq': ['Bequest (estate) tax', r'\tau^{BQ}_{t}}'],
    'T': ['Number of periods to steady-state', 'T'],
    'nu': ['Dampening parameter for TPI', r'\nu']
}
