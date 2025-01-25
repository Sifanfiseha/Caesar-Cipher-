# Caesar Cipher Message Encryption Code

This Python program implements a Caesar Cipher, which is a simple substitution cipher used for encoding and decoding messages. Below is a detailed explanation of how the code works and how to use it.

## How It Works

### Key Components:
1. **Alphabet List**: The `alphabet` list contains all lowercase English letters from `a` to `z`.

2. **Caesar Function**: The `ceaser` function performs the encoding or decoding of the input text. Here's a breakdown:
    - **Inputs**: The function takes three arguments:
      - `original_text`: The message to encode or decode.
      - `shift_amount`: The number of positions each letter in the text is shifted.
      - `encode_or_decode`: A string indicating whether to "encode" or "decode" the message.
    - **Logic**:
      - If the user wants to decode, the `shift_amount` is made negative.
      - For each letter in `original_text`, its position in the `alphabet` is shifted by `shift_amount`.
      - If the letter is not in the alphabet (e.g., a space or punctuation), it is added to the result as-is.
      - The result is printed with a message indicating whether it is encoded or decoded.

3. **Interactive Loop**: The program runs in a loop, allowing the user to:
    - Choose whether to encode or decode.
    - Input a message.
    - Provide a shift number.
    - Repeat the process or exit the program.

### Key Features:
- Handles wrapping around the alphabet using the modulo operator (`%`).
- Preserves non-alphabetical characters (e.g., spaces, punctuation).
- Allows case-insensitive input by converting the text to lowercase.

## How to Use

### Step-by-Step Instructions:
1. **Run the Program**: Execute the Python script in your terminal or IDE.

2. **Choose Action**: When prompted, type:
    - `encode` to encrypt a message.
    - `decode` to decrypt a message.

3. **Enter Message**: Type the message you want to process. The message can include letters, numbers, and special characters. Only letters will be shifted.

4. **Enter Shift Number**: Provide a positive integer for the shift. This determines how far each letter is shifted in the alphabet. For example:
    - A shift of 1 transforms `a` to `b`, `b` to `c`, and so on.
    - A shift of 27 is equivalent to a shift of 1, since the alphabet wraps around.

5. **View Result**: The program will display the encoded or decoded message.

6. **Repeat or Exit**: When asked, type:
    - `yes` to process another message.
    - `no` to exit the program.

### Example Usage:
#### Encode:
- Input:
  ```
  Type 'encode' to encrypt, type 'decode' to decrypt:
  encode
  Type your message:
  hello
  Type the shift number:
  5
  ```
- Output:
  ```
  Here is the encoded result: 'mjqqt'
  ```

#### Decode:
- Input:
  ```
  Type 'encode' to encrypt, type 'decode' to decrypt:
  decode
  Type your message:
  mjqqt
  Type the shift number:
  5
  ```
- Output:
  ```
  Here is the decoded result: 'hello'
  ```

## Notes:
- The shift amount should be a positive integer. Large numbers are automatically reduced to within the range of the alphabet length (26).
- Non-alphabetical characters are not shifted but remain in their original positions.

Enjoy encrypting and decrypting your messages with this Caesar Cipher!
