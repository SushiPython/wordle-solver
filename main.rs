use std::collections::HashSet;
use std::fs::File;
use std::io;
use std::io::Read;

#[derive(Debug, Clone)]
struct WordRestrictions {
    list_of_words: Vec<String>,
    anti_letters: Vec<char>,
    definitive_letters: String,
    possible_letters: Vec<char>,
    guessed_letters: Vec<char>,
    not_at_position: [HashSet<char>; 5]
}



fn main() {
    // assign words to var
    let list_of_words: Vec<String> = fetch_words();

    // restrictions definitions starting empty
    let anti_letters: Vec<char> = Vec::new();
    let definitive_letters: String = "00000".to_string();
    let possible_letters: Vec<char> = Vec::new();
    let guessed_letters: Vec<char> = Vec::new();
    let not_at_position: [HashSet<char>; 5] = Default::default();

    let word_restrictions = WordRestrictions {
        list_of_words,
        anti_letters,
        definitive_letters,
        possible_letters,
        guessed_letters,
        not_at_position
    };

    let mut base_word_restrictions = word_restrictions;

    let mut indice = 0;
    loop {
        let mut word: String = "tares".to_string();
        if indice > 0 {
            word = most_informative_word(&base_word_restrictions);
        }

        println!("{}", word);

        // get the colors for the word
        let colors = get_colors();

        // handle the color and word
        base_word_restrictions = handle_color_and_word(&word, &colors, &mut base_word_restrictions);
        // remove non possible words
        base_word_restrictions.list_of_words = get_possible_words(&base_word_restrictions);

        indice += 1;
    }
}

fn get_colors() -> String {
    // read user input
    let mut colors: String = String::new();
    io::stdin()
        .read_line(&mut colors)
        .expect("Failed to read input");

    colors.trim().to_string()
}

// find antiletters, definitive letters, and possible letters using the word and the color
fn handle_color_and_word(
    word: &str,
    color: &str,
    word_restrictions: &mut WordRestrictions,
) -> WordRestrictions {
    let word_chars: Vec<char> = word.chars().collect();
    // iterate over chars in word
    for (indice, char) in (0_i8..).zip(word_chars.clone().into_iter()) {
        if !word_restrictions.guessed_letters.contains(&char) {
            word_restrictions.guessed_letters.append(
                word_chars[indice as usize]
                    .to_string()
                    .chars()
                    .collect::<Vec<char>>()
                    .as_mut(),
            );
        }

        // get the char at color at indice
        let color_char: char = color.chars().nth(indice as usize).unwrap();
        if color_char == 'g' {
            // set definitive letters at position indice to char
            word_restrictions
                .definitive_letters
                .replace_range(indice as usize..indice as usize + 1, &char.to_string());
        } else if color_char == 'y' {
            word_restrictions.possible_letters.append(
                word_chars[indice as usize]
                    .to_string()
                    .chars()
                    .collect::<Vec<char>>()
                    .as_mut(),
            );
            word_restrictions.not_at_position[indice as usize].insert(char);
        } else if color_char == 'b' {
            word_restrictions.anti_letters.append(
                word_chars[indice as usize]
                    .to_string()
                    .chars()
                    .collect::<Vec<char>>()
                    .as_mut(),
            );
        }

    }

    word_restrictions.clone()
}

// fetch the words from files/words.txt
fn fetch_words() -> Vec<String> {
    let mut file = File::open("words.txt").expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("something went wrong reading the file");
    let words: Vec<String> = contents.split("\r\n").map(String::from).collect();
    words
}

// eliminate words that are not possible
fn get_possible_words(word_restrictions: &WordRestrictions) -> Vec<String> {
    let mut new_list_of_words: Vec<String> = Vec::new();
    for word in word_restrictions.list_of_words.clone() {
        let mut is_stage_five: bool = false;

        // iterate over chars in word
        let mut stage: i8 = 0;
        for i in 0..5 {
            if word_restrictions.definitive_letters.chars().nth(i).unwrap()
                == word.chars().nth(i).unwrap()
                || word_restrictions.definitive_letters.chars().nth(i).unwrap() == '0'
            {
                stage += 1
            }
        }
        for i in &word_restrictions.possible_letters {
            if !word.contains(&i.to_string()) {
                stage += -1
            }
        }
        for i in &word_restrictions.anti_letters {
            if word.contains(&i.to_string()) {
                stage += -1;
            }
        }
        for i in 0..5 {
            for j in &word_restrictions.not_at_position[i as usize] {
                if word.chars().nth(i as usize).unwrap() == *j {
                    stage += -1;
                }
            }
        }
        if stage == 5 {
            is_stage_five = true;
        }

        if is_stage_five {
            new_list_of_words.push(word);
        }
    }

    new_list_of_words
}

// calculate word informativeness score
fn get_word_score(word: &str, word_restrictions: &WordRestrictions) -> f32 {
    let mut score: f32 = 0.0;

    // iterate over chars in word
    let mut individual_chars: HashSet<char> = HashSet::new();
    for (indice, char) in (0_i8..).zip(word.chars()) {
        individual_chars.insert(char);

        // if the char is not in guessed_letters, subtract 2.0 from score
        if !word_restrictions.guessed_letters.contains(&char) {
            score += 1.5;
        }

        // if the char is not in possible_letters, at 1 to score
        if !word_restrictions.possible_letters.contains(&char) {
            score += 1.0;
        }

        // if the char index in word matches the char index in definitive_letters, subtract 1 from score
        let definitive_char: char = word_restrictions
            .definitive_letters
            .chars()
            .nth(indice.try_into().unwrap())
            .unwrap();

        if char == definitive_char {
            score -= 100.0;
        }

    }

    score += individual_chars.len() as f32;

    score
}

// find most informative word
fn most_informative_word(word_restrictions: &WordRestrictions) -> String {
    let mut most_informative_word: String = String::new();
    let mut most_informative_word_score: f32 = -500.0;
    for word in &word_restrictions.list_of_words {
        let word_score: f32 = get_word_score(word, word_restrictions);
        if word_score > most_informative_word_score {
            most_informative_word = word.to_string();
            most_informative_word_score = word_score;
        }
    }
    most_informative_word
}
