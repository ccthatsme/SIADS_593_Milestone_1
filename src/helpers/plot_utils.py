"""Helper functions for plotting data
"""

import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import widgets, Checkbox, Output, Layout, GridBox
from IPython.display import display, clear_output

def change_selection_type(selection, col_dtype):
    try:
        selection = [col_dtype.type(v) for v in selection]
    except Exception as e:
        print(f"Error converting selection to {col_dtype}: {e}")
        print("Falling back to integer type")
        selection = [int(v) if v.isdigit() else v for v in selection]
    return selection

def group_metric(df, group_cols, value_col="RAS", agg_func="median", out_name=None):
    result = df.groupby(group_cols)[value_col].agg(agg_func).reset_index()
    if out_name is not None:
        result = result.rename(columns={value_col: out_name})
    return result

def multiple_selection(selection):
    return len(selection) > 1

def plot_ras_series(ax, data, x_col, y_col, hue=None, title="", xlabel="Year", ylabel="RAS",
                    x_ticks=None, y_ticks=None, legend_title=None, legend_loc="best",
                    bbox_to_anchor=None, ncols=None):
    sns.lineplot(data=data, x=x_col, y=y_col, hue=hue, ax=ax)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if x_ticks is not None:
        ax.set_xticks(x_ticks)
        ax.set_xticklabels(x_ticks, rotation=45, ha="right")

    if y_ticks is not None:
        ax.set_yticks(y_ticks)

    ax.grid(True, alpha=0.3)

    if hue is not None:
        ax.legend(title=legend_title, loc=legend_loc, bbox_to_anchor=bbox_to_anchor, ncols=ncols)

def plot_lines(df, filter_col, selection, x_ticks, y_ticks):
    if len(selection) == 0:
        return
    
    col_dtype = df[filter_col].dtype

    selection = change_selection_type(selection, col_dtype)

    df_ras_filter_col = group_metric(
        df[df[filter_col].isin(selection)],
        ["Year", filter_col],
        value_col="RAS",
        agg_func="median",
        out_name="RAS"
    )

    df_var = group_metric(
        df_ras_filter_col,
        ["Year"],
        value_col="RAS",
        agg_func="var",
        out_name="Variance"
    )

    if not multiple_selection(selection):
        fig, ax = plt.subplots(figsize=(12, 6))
        plot_ras_series(
            ax,
            df_ras_filter_col,
            x_col="Year",
            y_col="RAS",
            hue=filter_col,
            title=f"Median RAS of Drafted NFL Player by {'Position(s)' if filter_col == 'POS' else 'Draft Round(s)'} each Year",
            ylabel="Median RAS",
            x_ticks=x_ticks,
            y_ticks=y_ticks,
            legend_title=f"{'Position' if filter_col == 'POS' else 'Draft Round'} (Selected)",
            bbox_to_anchor=(1.05, 1),
            legend_loc="lower right",
        )
        plt.tight_layout()
        plt.show()
    else:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

        plot_ras_series(
            ax1,
            df_ras_filter_col,
            x_col="Year",
            y_col="RAS",
            hue=filter_col,
            title=f"Median RAS of Drafted NFL Player by {'Position(s)' if filter_col == 'POS' else 'Draft Round(s)'} each Year",
            ylabel="Median RAS",
            x_ticks=x_ticks,
            y_ticks=y_ticks,
            legend_title=f"{'Position' if filter_col == 'POS' else 'Draft Round'} (Selected)",
            legend_loc="lower right",
            bbox_to_anchor=(1.05, 1),
            ncols=4,
        )

        plot_ras_series(
            ax2,
            df_var,
            x_col="Year",
            y_col="Variance",
            title=f"Variance of RAS Score Per Selected {'Position(s)' if filter_col == 'POS' else 'Draft Round(s)'} each Year",
            ylabel="Variance",
            x_ticks=x_ticks,
        )

        plt.tight_layout()
        plt.show()
    
def interactive_line_plot_checkboxes(df, filter_col, x_ticks, y_ticks):
    clear_output(wait=True)
    values = sorted(df[filter_col].dropna().unique())
    label = widgets.Label(f"Select {'Positions' if filter_col == 'POS' else 'Draft Rounds'}:")
    checkboxes = [Checkbox(
            value=bool(v == values[0] or v == values[1]),
            description=str(v)) for v in values]
    ui = GridBox(
    checkboxes,
    layout=Layout(
        grid_template_columns="repeat(4, 90px)",
        grid_gap="2px 5px",
        margin="0"
    )
    )
    out = Output()
    def update_plot(change):
        selected = [cb.description for cb in checkboxes if cb.value]
        out.clear_output(wait=True)
        with out:
            plot_lines(df, filter_col, selected, x_ticks, y_ticks)

    for cb in checkboxes:
        cb.unobserve_all()
        cb.observe(update_plot, "value")
        update_plot(None)

    display(label, ui, out)