openapi: 3.0.0
info:
  title: LangChain Agent API
  version: 1.0.0
paths:
  /parse-yaml-metadata:
    post:
      summary: Parses YAML metadata from a string
      operationId: parseYamlMetadata
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                yaml_content:
                  type: string
      responses:
        '200':
          description: Parsed metadata
          content:
            application/json:
              schema:
                type: object

  /parse-table:
    post:
      summary: Parses table content into a Table object
      operationId: parseTableData
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                table_content:
                  type: string
      responses:
        '200':
          description: Table object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Table'

  /parse-python-script:
    post:
      summary: Parses a Python script into a SourceCode object
      requestBody:
        operationId: parsePythonScript
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                script:
                  type: string
      responses:
        '200':
          description: SourceCode object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SourceCode'

  /parse-markdown-content:
    post:
      summary: Parses Markdown content into a MarkdownDocument object
      requestBody:
        operationId: parseMarkdownContent
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                markdown_path:
                  type: string
      responses:
        '200':
          description: MarkdownDocument object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MarkdownDocument'

  /minio-action:
    post:
      summary: Perform an action with MinIO client
      requestBody:
      operationId: minioAction
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MinioRequest'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MinioResponse'
        '500':
          description: Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

  /weaviate-action:
    post:
      summary: Perform an action with Weaviate client
      requestBody:
      operationId: weaviateAction
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WeaviateRequest'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WeaviateResponse'
        '500':
          description: Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

components:
  securitySchemes:
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://example.com/oauth/authorize
          tokenUrl: https://example.com/oauth/token
          scopes:
            read: Read access
            write: Write access
  schemas:
    MinioRequest:
      type: object
      properties:
        bucket_name:
          type: string
        object_name:
          type: string
      required:
        - bucket_name
        - object_name

    WeaviateRequest:
      type: object
      properties:
        class_name:
          type: string
        properties:
          type: object
      required:
        - class_name
        - properties

    MinioResponse:
      type: object
      properties:
        message:
          type: string
        data:
          type: string

    WeaviateResponse:
      type: object
      properties:
        message:
          type: string

    ErrorResponse:
      type: object
      properties:
        detail:
          type: string
          
    Table:
      type: object
      properties:
        headers:
          type: array
          items:
            type: string
          description: Headers of the table
        rows:
          type: array
          items:
            type: object
            additionalProperties: true
          description: Rows of the table, each row being a dictionary
      description: Represents a table with headers and rows

    SourceCode:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the source code object
        imports:
          type: array
          items:
            type: string
          description: List of extracted required packages
        classes:
          type: array
          items:
            type: string
          description: List of extracted classes from the code
        code:
          type: string
          description: Source code snippets
        syntax:
          type: string
          description: The programming language syntax/extension (e.g., Python)
        context:
          type: string
          description: Any extracted text, markdown, comments, or docstrings
        metadata:
          type: object
          additionalProperties: true
          description: Extracted or generated metadata tags for top-level cataloging and code object management
      description: Represents a source code block with related metadata

    MarkdownDocument:
      type: object
      properties:
        metadata:
          type: object
          additionalProperties: true
          description: Metadata of the document
        tables:
          type: array
          items:
            $ref: '#/components/schemas/Table'
          description: List of tables in the document
        code_blocks:
          type: array
          items:
            $ref: '#/components/schemas/SourceCode'
          description: List of code blocks in the document
        content:
          type: string
          description: The textual content of the document
      description: Represents a Markdown document including metadata, tables, and code blocks
    Notification:
      type: object
      properties:
        Records:
          type: array
          items:
            type: object
            properties:
              s3:
                type: object
                properties:
                  bucket:
                    type: object
                    properties:
                      name:
                        type: string
                  object:
                    type: object
                    properties:
                      key:
                        type: string



          

openapi: 3.0.0
info:
  title: Custom API-AI Gateway for MinIO LANGCHAIN and Weaviate
  version: 1.0.0
servers:
  - url: https://api.example.com
    description: Main production server
paths:
  /health:
    get:
      summary: Health Check Endpoint
      operationId: getHealthCheck
      responses:
        '200':
          description: Returns the health status of the API
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
  /:
    get:
      summary: Root Endpoint
      operationId: getRoot
      responses:
        '200':
          description: Welcome message
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
  /minio-events/:
    post:
      summary: Handle MinIO Event
      operationId: postMinioEvent
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                eventType:
                  type: string
                eventData:
                  type: object
                  additionalProperties: true
      responses:
        '200':
          description: Acknowledgement of the event
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
  /minio-webhook/:
    post:
      summary: Handle MinIO Webhook
      operationId: postMinioWebhook
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Notification'
      responses:
        '200':
          description: Results of the webhook processing
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  results:
                    type: array
                    items:
                      type: object
                  errors:
                    type: array
                    items:
                      type: object
  /process/{bucket_name}:
    get:
      summary: Process Specified Bucket
      operationId: getProcessBucket
      parameters:
        - in: path
          name: bucket_name
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Response after processing the bucket
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    post:
      summary: Process Specified Bucket
      operationId: postProcessBucket
      parameters:
        - in: path
          name: bucket_name
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Response after processing the bucket
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
  /upload-clean-data:
    post:
      summary: Upload and Process Clean Data
      operationId: postUploadCleanData
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
      responses:
        '200':
          description: Acknowledgement of file upload and processing
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
  /get-code-snippet:
    get:
      summary: Retrieve a Code Snippet
      operationId: getCodeSnippet
      responses:
        '200':
          description: Returns the requested code snippet
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: string

components:
  securitySchemes:
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://example.com/oauth/authorize
          tokenUrl: https://example.com/oauth/token
          scopes:
            read: Read access
            write: Write access