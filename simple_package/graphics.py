import matplotlib.pyplot as plt
import numpy as np

def plot_histogram_with_stats(data, title="Data Distribution", xlabel="Values", ylabel="Frequency", bins='auto'):
    """
    Plot a histogram of data with mean and median marked.
    """
    
    # Calculate statistics
    mean_val = np.mean(data)
    median_val = np.median(data)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot histogram
    plt.hist(data, bins=bins, alpha=0.7, color='skyblue', edgecolor='black', label='Data')
    
    # Add vertical lines for mean and median
    plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
    plt.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median: {median_val:.2f}')
    
    # Customize the plot
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(alpha=0.3)
    plt.legend()
    
    # Add some statistics as text
    stats_text = f'Count: {len(data)}\nStd Dev: {np.std(data):.2f}'
    plt.annotate(stats_text, xy=(0.02, 0.98), xycoords='axes fraction', 
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
                verticalalignment='top', fontsize=10)
    
    plt.tight_layout()
    return plt.gcf()

# Example usage when run directly
if __name__ == "__main__":
    # Generate sample data for demonstration
    rng = np.random.seed(42)
    sample_data = rng.normal(50, 15, 1000)
    
    # Plot the histogram
    plot_histogram_with_stats(sample_data, "Sample Data Distribution", "Values", "Frequency")
    
    # Save and show
    plt.savefig('histogram_example.png')
    plt.show()