class Custom():
    def get_trend(self,data,x,metrics):
        n_met = len(metrics)
        fig, ax = plt.subplots(figsize=(15, 5))

        for met in metrics:
            plt.plot(data[x], data[met],label=met)
        plt.xlabel(x)
        plt.ylabel('metrics')
        plt.legend(loc='best')

    def get_resid_plot(self,actual,pred,norm=True):
        residual = actual-pred
        norm_resid = preprocessing.normalize([residual])
        resid_zero = np.zeros(len(residual))
        if norm:
            residual = norm_resid

        a,b = best_fit(pred,residual)
    #     print (len(a),len(b))
        yfit = [a + b * xi for xi in pred]

        fig, ax = plt.subplots(figsize=(15, 5))
    #     plt.plot(pred,resid_zero, color='red', linewidth=1, linestyle= '---')
        ax.scatter(pred, residual, c='black', alpha=0.3, edgecolors='none')
    #     plt.plot(pred,yfit, color='grey', linewidth=0.5, linestyle= '--')
        ax.legend()
        ax.grid(False)
        plt.xlabel('pred')
        plt.ylabel('residual')
        plt.legend(loc='best')


