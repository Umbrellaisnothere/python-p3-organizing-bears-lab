select_all_female_bears_return_name_and_age = """
    SELECT bears.name, bears.age FROM bears WHERE bears.sex = "F";
"""

select_all_male_bears_return_name_and_age = """
    SELECT bears.name, bears.age FROM bears WHERE bears.sex = "M":
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT bears.name FROM bears ORDER BY bears.name;
"""

select_all_bears_names_and_ages_that_are_alive = """
    SELECT bears.name, bears.age FROM bears WHERE bears.alive = true;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_oldest_to_youngest = """
    SELECT bears.name, bears.age FROM bears WHERE bears.alive = true ORDER BY bears.age DESC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT bears.name, bears.age FROM bears WHERE bears.alive = true ORDER BY bears.age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT bears.name, bears.age FROM bears ORDER BY bears.age DESC LIMIT 1;
"""

select_youngest_bear_and_returns_name_and_age = """
    SELECT bears.name, bears.age FROM bears ORDER BY bears.age ASC LIMIT 1;
"""

# select_average_age_of_all_bears = """
#     SELECT AVG(bears.age) FROM bears;
# """

