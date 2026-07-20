void process()
{
    feature_info(power, quality, median);
    for (int i = 0; i < MAX_FEATURES; ++i)
    {
        prevFeature[i] = 0;
    }
 
    for (int t = 0; t < TIME_STEPS; ++t)
    {
        user_info(currentUser);
        double W[MAX_FEATURES] = {0};
        for (int i = 0; i < MAX_FEATURES; ++i)
        {
            for (int u = 0; u < MAX_USERS; ++u)
            {
                W[i] += (quality[i] * 0.01) / (ABS(median[i] - currentUser[u]) + 1.0);
            }
        }
 
        double low = 0.0;
        double high = 100000.0;
        int best_v[MAX_FEATURES] = {0};
 
        for (int iter = 0; iter < 50; ++iter)
        {
            double mu = (low + high) / 2.0;
            double current_total_power = 0.0;
            int temp_v[MAX_FEATURES] = {0};
 
            for (int i = 0; i < MAX_FEATURES; ++i)
            {
                double max_score = -1e9;
                int opt_v = 0;
                for (int v = 0; v <= 100; ++v)
                {
                    double p_cost = ((power[i] * v * v) / 10000.0) + (0.01 * ABS(prevFeature[i] - v));
                    double score = (W[i] * v) - mu * p_cost;
 
                    if (score > max_score)
                    {
                        max_score = score;
                        opt_v = v;
                    }
                }
                temp_v[i] = opt_v;
                current_total_power += ((power[i] * temp_v[i] * temp_v[i]) / 10000.0) + (0.01 * ABS(prevFeature[i] - temp_v[i]));
            }
 
            if (current_total_power < POWER_BUDGET)
            {
                for (int i = 0; i < MAX_FEATURES; ++i)
                {
                    best_v[i] = temp_v[i];
                }
                high = mu;
            } else
            {
                low = mu;
            }
        }
 
        screen_control((best_v));
        for (int i = 0; i < MAX_FEATURES; ++i)
        {
            prevFeature[i] = best_v[i];
        }
    }
}